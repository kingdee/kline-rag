import argparse
import os
from utils.embedding import EmbeddingModel
from utils.chunker import chunk_markdown_by_folder
from utils.faiss_indexer import FaissIndexer
from utils.retrievers import RetrieverFactory

from typing import Annotated
from fastmcp import FastMCP

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)



GLOBAL_RETRIEVER = None

def init_embedding_model(url, api_key, model_name):

    return EmbeddingModel(api_key=api_key, url=url, model_name=model_name)

def init_vector_store(emdding_model: EmbeddingModel, doc_dir: str, vector_store_path: str):
    global GLOBAL_RETRIEVER

    # 1. 加载所有 markdown 文档
    docs = chunk_markdown_by_folder(doc_dir)

    # 2. 初始化 indexer
    indexer = FaissIndexer(emdding_model)

    # 3. 强制重新构建向量库，并覆盖之前的内容
    store = indexer.build_from_documents(docs, save_path=vector_store_path)

    # 4. 构建相似度引用器
    GLOBAL_RETRIEVER = RetrieverFactory.similarity(store)

    print("Vector store builted successfully!")


def get_rag_content(query: str, k: int = 10) -> str:
    if GLOBAL_RETRIEVER is None:
        return "ERROR: Vector store not initialized."
    
    GLOBAL_RETRIEVER.search_kwargs["k"] = k
    results = GLOBAL_RETRIEVER.invoke(query)
    return "\n---\n".join([d.page_content for d in results])


mcp = FastMCP(name="KWCRagServer")


@mcp.tool
def get_kwc_documentation(
        query: Annotated[str, "用户的查询内容、KWC使用及说明的任何相关文本，尽可能是多个完整的组件名称，以便召回更全面、详细的使用文档。"],
        k: Annotated[int, "用于控制从知识库中检索的、与查询最相关的文档的最大数量。"]) -> str:
    """
    根据用户的查询内容，返回KWC使用及说明的相关文档，以帮助模型编写KWC代码。
    目前已有组件：复选框(kd-checkbox)、复选框组(kd-checkbox-group)、输入框(kd-input)、数值输入框(kd-input-number)、单选框(kd-radio)、单选框组(kd-radio-group)、按钮(kd-button)、按钮菜单(kd-button-menu)、图标(kd-icon)、标签(kd-tag)、卡片(kd-card)、表格(kd-table)、布局(kd-layout)、选项卡(kd-tabset)、消息提示(kd-toast)
    """
    return get_rag_content(query, k)


if __name__ == "__main__":
    # embdding model config
    URL = "https://api.siliconflow.cn/v1/embeddings"
    MODEL_NAME = "BAAI/bge-m3"
    API_KEY = "Bearer sk-dtolptxpexqpplrfbwmcbjwqcgswqqrujsrwudorashysmvz"

    doc_dir = "doc/kwc_doc"
    vector_store_path = "vector_store/faiss_bge_m3_kwc"

    embedding_model = init_embedding_model(URL, API_KEY, MODEL_NAME)

    init_vector_store(embedding_model, doc_dir, vector_store_path)

    # 启动服务
    mcp.run(transport="sse", host="0.0.0.0", port=8003)
