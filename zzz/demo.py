import argparse
from utils.embedding import EmbeddingModel
from utils.chunker import load_and_chunk
from utils.tfidf_retriever import SimpleTfidfRetriever
from utils.faiss_indexer import FaissIndexer
from utils.retrievers import RetrieverFactory
from utils.reranker import CrossEncoderReranker


def main(md_path: str, api_key: str, url: str, model_name: str, k: int = 5):
    emb = EmbeddingModel(api_key=api_key, url=url, model_name=model_name)
    docs = load_and_chunk(md_path)

    # build index
    indexer = FaissIndexer(emb)
    store = indexer.build_from_documents(docs)

    # tfidf
    # tfidf = SimpleTfidfRetriever()
    # tfidf.build(docs)


    query = "帮我使用kwc创建一个按钮"

    print("--- similarity retriever ---")
    sim = RetrieverFactory.similarity(store, k=k)
    for d in sim.invoke(query):
        print(d)

    # print("--- ensemble hybrid ---")
    # ensemble = RetrieverFactory.ensemble_hybrid(store, tfidf, k=k)
    # for d in ensemble.get_relevant_documents(query):
    #     print(d.metadata, d.page_content[:200].replace("\n", " "))

    # print("--- rerank top20 ---")
    # top20 = RetrieverFactory.similarity(store, k=20).get_relevant_documents(query)
    # reranker = CrossEncoderReranker()
    # reranked = reranker.rerank(query, top20)
    # for doc, score in reranked[:5]:
    #     print(score, doc.metadata)




if __name__ == '__main__':
    Siliconflow_URL = "https://api.siliconflow.cn/v1/embeddings"
    Zenithal_URL = "http://ai.zenithal.ai:32520/v1/embeddings"
    Model_Name = "bge-m3"

    API_KEY = "Bearer sk-dtolptxpexqpplrfbwmcbjwqcgswqqrujsrwudorashysmvz"
    markdown_file = "/Users/_diyigelieren/Documents/Kingdee/KWC/kwc_rag/kwc_doc/KWC_Developer_Documentation.md"
    
    main(md_path=markdown_file, 
         api_key=API_KEY, 
         url=Zenithal_URL, 
         model_name=Model_Name,     
         k=1)