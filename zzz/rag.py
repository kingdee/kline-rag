from typing import List, Tuple, Dict, Any
import os
import numpy as np
import requests

from langchain.schema import Document
from langchain.text_splitter import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

# Vector store / retriever
from langchain_community.vectorstores import FAISS
from langchain.embeddings.base import Embeddings
from langchain.retrievers import EnsembleRetriever, MultiQueryRetriever

# sparse
from sklearn.feature_extraction.text import TfidfVectorizer

# cross-encoder reranker
from sentence_transformers import CrossEncoder  # pip install sentence-transformers

# -------------------------
# 1) 自定义 Embeddings（对接“硅基流动”的 embedding API）
# -------------------------

class EmbeddingModel(Embeddings):
    """
    Authorization: "Bearer sk-dtolptxpexqpplrfbwmcbjwqcgswqqrujsrwudorashysmvz"
    """
    def __init__(self, api_key: str, url: str="https://api.siliconflow.cn/v1/embeddings", model_name: str = "BAAI/bge-m3"):
        self.api_key = api_key
        self.url = url
        self.model_name = model_name

    def _call_api(self, texts: List[str]) -> List[List[float]]:
        try:
            payload = {
                "model": self.model_name,
                "input": texts,
                "encoding_format": "float"
            }
            headers = {
                "Authorization": self.api_key,
                "Content-Type": "application/json"
            }

            response = requests.post(self.url, json=payload, headers=headers)
            post_response = []
            for r in response.json().get("data", []):
                post_response.append(r.get("embedding", []))

            return post_response
        
        except Exception as e:
            print(f"Error calling embedding API: {e}")
            return [[0.0]*1024]*len(texts)  
        

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._call_api(texts)

    def embed_query(self, text: str) -> List[float]:
        return self._call_api([text])[0]

# -------------------------
# 2) 加载 .md 并做分块（优先 header 分块）
# -------------------------
def load_and_chunk(md_path: str) -> List[Document]:
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 只用 MarkdownHeaderTextSplitter 按标题切分
    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[
            ("#", "Header 1"),
            ("##", "Header 2"),
            ("###", "Header 3"),
            ("####", "Header 4"),
        ],
        strip_headers=False
    )
    docs = header_splitter.split_text(text)

    # 给每个分块加上文件名元数据
    for i, doc in enumerate(docs):
        doc.metadata.update({
            "source": os.path.basename(md_path),
            "chunk_index": i
        })

    return docs


# -------------------------
# 3) 建向量库（FAISS）
# -------------------------
def build_faiss(docs: List[Document], emb: EmbeddingModel, index_path: str = None) -> FAISS:
    """
    不用
    """
    texts = [d.page_content for d in docs]
    vectors = emb.embed_documents(texts)
    vecs = np.array(vectors).astype("float32")

    # 归一化以便用内积作为 cosine 近似（可选）
    vecs = vecs / (np.linalg.norm(vecs, axis=1, keepdims=True) + 1e-12)
    # 使用 LangChain 的 FAISS wrapper（需要传 embeddings）
    faiss_store = FAISS.from_documents(docs, emb)  # LangChain 会内建做向量化（但这里实现了 embed）

    # 如果你想直接使用已有向量并自建索引，可以使用 faiss.IndexFlatIP；此处用简洁API
    if index_path:
        faiss_store.save_local(index_path)
    return faiss_store


# -------------------------
# 4) 稀疏检索器（TF-IDF）—用于混合
# -------------------------
class SimpleTfidfRetriever:
    def __init__(self):
        self.vec = TfidfVectorizer(ngram_range=(1,2), max_features=50000)
        self.docs: List[Document] = []
        self.matrix = None

    def build(self, docs: List[Document]):
        self.docs = docs
        corpus = [d.page_content for d in docs]
        self.matrix = self.vec.fit_transform(corpus)

    def get_relevant_documents(self, query: str, k: int = 5) -> List[Document]:
        qv = self.vec.transform([query])
        scores = (self.matrix @ qv.T).toarray().ravel()
        idxs = np.argsort(scores)[::-1][:k]
        return [self.docs[i] for i in idxs if scores[i] > 0]

# -------------------------
# 5) 检索策略示例实现
# -------------------------

def similarity_retriever(faiss_store: FAISS, k: int = 5):
    """
    向量相似度检索（默认 similarity）
    """
    retriever = faiss_store.as_retriever(search_type="similarity", search_kwargs={"k": k})
    return retriever

def mmr_retriever(faiss_store: FAISS, k: int = 5, fetch_k: int = 20):
    """
    MMR 检索：兼顾相关性与多样性
    - fetch_k: 先检索前 fetch_k 个，再用 MMR 选 k 个
    """
    retriever = faiss_store.as_retriever(search_type="mmr", search_kwargs={"k": k, "fetch_k": fetch_k})
    return retriever

def threshold_retriever(faiss_store: FAISS, k: int = 10, score_threshold: float = 0.2):
    """
    相似度阈值过滤（需要 VectorStore 支持 similarity_score_threshold）
    """
    retriever = faiss_store.as_retriever(search_type="similarity",
                                         search_kwargs={"k": k, "score_threshold": score_threshold})
    return retriever

def ensemble_hybrid_retriever(faiss_store: FAISS, tfidf_retriever: SimpleTfidfRetriever, k: int = 5):
    """
    稠密 + 稀疏 混合检索
    使用 LangChain 的 EnsembleRetriever 将两个 retriever 的结果合并（加权）
    注意：EnsembleRetriever 要求传入 retrievers 列表和 weights 列表
    """
    # 将 SimpleTfidfRetriever 包装成 LangChain 风格的对象（只需实现 get_relevant_documents）
    class TfidfWrapper:
        def __init__(self, tfidf):
            self._tfidf = tfidf
        def get_relevant_documents(self, query, k=5):
            return self._tfidf.get_relevant_documents(query, k=k)

    dense = faiss_store.as_retriever(search_type="similarity", search_kwargs={"k": k})
    sparse = TfidfWrapper(tfidf_retriever)
    ensemble = EnsembleRetriever(retrievers=[dense, sparse], weights=[0.6, 0.4])
    return ensemble

def rerank_with_cross_encoder(faiss_store: FAISS, query: str, top_k: int = 20, rerank_model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
    """
    先用向量库粗排 top_k，然后用 CrossEncoder（sentence-transformers）对 doc+query 重排得分
    返回按重排分数排序后的 doc 列表（包含score）
    """
    # 先粗排
    retriever = faiss_store.as_retriever(search_type="similarity", search_kwargs={"k": top_k})
    candidates = retriever.get_relevant_documents(query)
    # 加载 cross-encoder
    reranker = CrossEncoder(rerank_model_name, device="cpu")  # 若有 GPU 用 "cuda"
    # cross-encoder 要求每个 item 是 (query, doc_text)
    pairs = [(query, c.page_content) for c in candidates]
    scores = reranker.predict(pairs)  # 返回一维分数数组
    # 组合并排序
    scored = list(zip(candidates, scores))
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored  # [(Document, score), ...]

def multquery_retriever_example(faiss_store: FAISS, llm, query: str, k_per_query: int = 5):
    """
    MultiQueryRetriever 示例：
    - 先用 LLM 将用户 query 拆成多个子 query（提示模板可定制）
    - 并行对每个子query检索，再合并结果
    LangChain 提供 MultiQueryRetriever，但常见做法是自己用 LLM 改写后合并。
    这里使用 LangChain 的 MultiQueryRetriever 简化演示（需要 LangChain 支持的版本）。
    """
    # 简洁起见，使用 LangChain 自带 MultiQueryRetriever：需要传入基础 retriever 和 LLM
    base_retriever = faiss_store.as_retriever(search_type="similarity", search_kwargs={"k": k_per_query})
    mqr = MultiQueryRetriever.from_retriever(llm=llm, retriever=base_retriever)
    docs = mqr.get_relevant_documents(query)
    return docs

# -------------------------
# 6) 使用示例主流程
# -------------------------
def demo_flow(md_path: str, api_key: str, url: str, model_name: str, k: int = 5):
    emb = EmbeddingModel(api_key=api_key, url=url, model_name=model_name)
    docs = load_and_chunk(md_path)
    # build FAISS (LangChain 会在内部调用 embeddings)
    faiss_store = FAISS.from_documents(docs, emb)

    # build TFIDF
    tfidf = SimpleTfidfRetriever()
    tfidf.build(docs)

    query = "帮我使用kwc创建一个按钮"

    print("=== similarity ===")
    sim_ret = similarity_retriever(faiss_store, k)
    for d in sim_ret.invoke(query):
        # print(d.metadata, d.page_content[:200].replace("\n"," "), "...")
        print(d)

    # print("\n=== mmr ===")
    # mmr_ret = mmr_retriever(faiss_store, k=5, fetch_k=20)
    # for d in mmr_ret.get_relevant_documents(query):
    #     print(d.metadata, d.page_content[:160].replace("\n"," "), "...")

    # print("\n=== threshold (score filter) ===")
    # thr_ret = threshold_retriever(faiss_store, k=10, score_threshold=0.25)
    # for d in thr_ret.get_relevant_documents(query):
    #     print(d.metadata, d.page_content[:160].replace("\n"," "), "...")

    # print("\n=== hybrid ensemble (dense + tfidf) ===")
    # ensemble = ensemble_hybrid_retriever(faiss_store, tfidf, k=5)
    # for d in ensemble.get_relevant_documents(query):
    #     print(d.metadata, d.page_content[:160].replace("\n"," "), "...")

    # print("\n=== rerank with cross-encoder ===")
    # reranked = rerank_with_cross_encoder(faiss_store, query, top_k=20)
    # for doc, score in reranked[:5]:
    #     print(score, doc.metadata, doc.page_content[:140].replace("\n"," "), "...")

    # print("\n=== multiquery retriever (LLM rewrite) ===")
    # mdocs = multquery_retriever_example(faiss_store, llm, query, k_per_query=4)
    # for d in mdocs[:8]:
    #     print(d.metadata, d.page_content[:140].replace("\n"," "), "...")

if __name__ == "__main__":
    Siliconflow_URL = "https://api.siliconflow.cn/v1/embeddings"
    Zenithal_URL = "http://ai.zenithal.ai:32314/v1/embeddings"
    Model_Name = "bge-m3"

    API_KEY = "Bearer sk-dtolptxpexqpplrfbwmcbjwqcgswqqrujsrwudorashysmvz"
    markdown_file = "/Users/_diyigelieren/Documents/Kingdee/KWC/kwc_rag/kwc_doc/KWC_Developer_Documentation.md"
    demo_flow(md_path=markdown_file, api_key=API_KEY, url=Zenithal_URL, model_name=Model_Name, k=1)