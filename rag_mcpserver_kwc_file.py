import argparse
import os
from utils.embedding import EmbeddingModel
from utils.chunker import chunk_markdown_by_headers
from utils.tfidf_retriever import SimpleTfidfRetriever
from utils.faiss_indexer import FaissIndexer
from utils.retrievers import RetrieverFactory
from utils.reranker import CrossEncoderReranker

from typing import Annotated
from fastmcp import FastMCP


def get_rag_content(query:str, k: int = 10, vector_store_path: str = None):
    URL = "https://api.siliconflow.cn/v1/embeddings"
    MODEL_NAME = "BAAI/bge-m3"

    API_KEY = "Bearer xxx"
    MARKDOWN_FILE = "./kwc_doc/KWC_Developer_Documentation.md"

    emb = EmbeddingModel(api_key=API_KEY, url=URL, model_name=MODEL_NAME)
    docs = chunk_markdown_by_headers(MARKDOWN_FILE)

    # build index
    indexer = FaissIndexer(emb)

    if vector_store_path:
        if os.path.isdir(vector_store_path):
            try:
                store = indexer.load(vector_store_path)
            except Exception as e:
                print(f"Failed to load existing vector store from {vector_store_path}: {e}")
                print("Rebuilding the vector store...")
                store = indexer.build_from_documents(docs, save_path=vector_store_path)
        else:
            print(f"Vector store path {vector_store_path} does not exist. Building new vector store...")
            store = indexer.build_from_documents(docs, save_path=vector_store_path)
    else:
        store = indexer.build_from_documents(docs, save_path=None)

    sim = RetrieverFactory.similarity(store, k=k)

    page_contents = []
    for d in sim.invoke(query):
        page_contents.append(d.page_content)
    
    return "\n---\n".join(page_contents)


mcp = FastMCP(name="KWCRagServer")
@mcp.tool
def get_kwc_documentation(query: Annotated[str, "用户的查询内容、KWC使用及说明的任何相关文本"]) -> str:
    """
    根据用户的查询内容，返回KWC使用及说明的相关文档，以帮助模型编写KWC代码。
    """
    vector_store_path = "./vector_store/faiss_bge_m3_kwc"
    return get_rag_content(query=query, vector_store_path=vector_store_path)




if __name__ == "__main__":
    mcp.run(transport="sse", host="127.0.0.1", port=8002)