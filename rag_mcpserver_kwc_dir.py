import argparse
import os
from utils.embedding import EmbeddingModel
from utils.chunker import chunk_markdown_by_folder
from utils.tfidf_retriever import SimpleTfidfRetriever
from utils.faiss_indexer import FaissIndexer
from utils.retrievers import RetrieverFactory
from utils.reranker import CrossEncoderReranker

from typing import Annotated
from fastmcp import FastMCP


def get_rag_content(query:str, k: int = 10, doc_dir: str = None, vector_store_path: str = None):
    URL = "https://api.siliconflow.cn/v1/embeddings"
    MODEL_NAME = "BAAI/bge-m3"
    # URL = "http://ai.zenithal.ai:32520/v1/embeddings"
    # MODEL_NAME = "bge-m3"

    API_KEY = "Bearer sk-dtolptxpexqpplrfbwmcbjwqcgswqqrujsrwudorashysmvz"
    MARKDOWN_DIR = doc_dir

    emb = EmbeddingModel(api_key=API_KEY, url=URL, model_name=MODEL_NAME)
    docs = chunk_markdown_by_folder(MARKDOWN_DIR)

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


# 目前已有组件：复选框(kd-checkbox)、复选框组(kd-checkbox-group)、输入框(kd-input)、数值输入框(kd-input-number)、单选框(kd-radio)、单选框组(kd-radio-group)、按钮(kd-button)、按钮菜单(kd-button-menu)、图标(kd-icon)、标签(kd-tag)、卡片(kd-card)、表格(kd-table)、布局(kd-layout)、选项卡(kd-tabset)、消息提示(kd-toast)

mcp = FastMCP(name="KWCRagServer")
@mcp.tool
def get_kwc_documentation(query: Annotated[str, "用户的查询内容、KWC使用及说明的任何相关文本，尽可能是多个完整的组件名称，以便召回更全面、详细的使用文档。"]) -> str:
    """
    根据用户的查询内容，返回KWC使用及说明的相关文档，以帮助模型编写KWC代码。
    目前已有组件：复选框(kd-checkbox)、复选框组(kd-checkbox-group)、输入框(kd-input)、数值输入框(kd-input-number)、单选框(kd-radio)、单选框组(kd-radio-group)、按钮(kd-button)、按钮菜单(kd-button-menu)、图标(kd-icon)、标签(kd-tag)、卡片(kd-card)、表格(kd-table)、布局(kd-layout)、选项卡(kd-tabset)、消息提示(kd-toast)
    """
    doc_dir = "./doc/kwc_doc_real_v2"
    vector_store_path = "./vector_store/faiss_bge_m3_kwc_real_v2"
    return get_rag_content(query=query, doc_dir=doc_dir, k=10, vector_store_path=vector_store_path)



if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8003)
    # print(get_kwc_documentation("复选框"))