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



GLOBAL_DOC_RETRIEVER = None
GLOBAL_CODE_RETRIEVER = None

def init_embedding_model(url, api_key, model_name):

    return EmbeddingModel(api_key=api_key, url=url, model_name=model_name)

def init_doc_vector_store(emdding_model: EmbeddingModel, docs_dir: str, vector_store_path: str):
    global GLOBAL_DOC_RETRIEVER

    # 1. 加载所有 markdown 文档
    docs = chunk_markdown_by_folder(docs_dir)
    # 2. 初始化 indexer
    indexer = FaissIndexer(emdding_model)
    # 3. 构建向量库
    store = indexer.build_from_documents(docs, save_path=vector_store_path)
    # 4. 构建相似度引用器
    GLOBAL_DOC_RETRIEVER = RetrieverFactory.similarity(store)

    print("Vector doc store builted successfully!")


def init_code_vector_store(emdding_model: EmbeddingModel, docs_dir: str, vector_store_path: str):
    global GLOBAL_CODE_RETRIEVER

    # 1. 加载所有 markdown 文档
    docs = chunk_markdown_by_folder(docs_dir)
    # 2. 初始化 indexer
    indexer = FaissIndexer(emdding_model)
    # 3. 构建向量库
    store = indexer.build_from_documents(docs, save_path=vector_store_path)
    # 4. 构建相似度引用器
    GLOBAL_CODE_RETRIEVER = RetrieverFactory.similarity(store)

    print("Vector code store builted successfully!")


def get_doc_content(query: str, k: int = 10) -> str:
    if GLOBAL_DOC_RETRIEVER is None:
        return "ERROR: Doc vector store not initialized."

    GLOBAL_DOC_RETRIEVER.search_kwargs["k"] = k
    results = GLOBAL_DOC_RETRIEVER.invoke(query)
    return "\n---\n".join([d.page_content for d in results])

def get_code_content(query: str, k: int = 10) -> str:
    if GLOBAL_CODE_RETRIEVER is None:
        return "ERROR: Code vector store not initialized."

    GLOBAL_CODE_RETRIEVER.search_kwargs["k"] = k
    results = GLOBAL_CODE_RETRIEVER.invoke(query)
    return "\n---\n".join([d.page_content for d in results])


mcp = FastMCP(name="KWCRagServer")


@mcp.tool
def get_kwc_documentation(
        query: Annotated[str, "用户的查询内容、KWC使用及说明的任何相关文本，尽可能是多个完整的组件名称，以便召回更全面、详细的使用文档。"],
        k: Annotated[int, "用于控制从知识库中检索的、与查询最相关的文档的最大数量。\n 说明: 一个chuck就是一个完整的原子组件文档。"]) -> str:
    """
    根据用户的查询内容，返回KWC使用及说明的相关文档，以帮助模型编写KWC代码。
    目前已有组件：复选框(kd-checkbox)、复选框组(kd-checkbox-group)、输入框(kd-input)、数值输入框(kd-input-number)、按钮(kd-button)、按钮菜单(kd-button-menu)、图标(kd-icon)、标签(kd-tag)、卡片(kd-card)、表格(kd-datatable)、布局(kd-layout)、选项卡(kd-tabset)
    """
    return get_doc_content(query, k)

@mcp.tool
def get_kwc_code_examples(
        query: Annotated[str, "用户的查询内容、KWC代码示例的任何相关文本，尽可能是一个场景的完整描述，以便召回更全面、详细的代码示例。"],
        k: Annotated[int, "用于控制从代码知识库中检索的、与查询最相关的代码示例的最大数量。\n 说明: 一个chuck就是一个完整的代码示例组件文档。"]) -> str:
    """
    根据用户的查询内容，返回KWC代码示例的相关文档，以帮助模型编写KWC代码。
    """
    return get_code_content(query, k)

if __name__ == "__main__":
    # embdding model config
    URL = "https://api.siliconflow.cn/v1/embeddings"
    MODEL_NAME = "BAAI/bge-m3"
    API_KEY = "Bearer sk-dtolptxpexqpplrfbwmcbjwqcgswqqrujsrwudorashysmvz"

    # 文档路径和向量库存储路径
    doc_dir = "docs/kwc_doc"
    doc_vector_store_path = "vector_store/faiss_bge_m3_kwc_doc"

    # 示例代码路径和向量库存储路径
    code_dir = "docs/kwc_code"
    code_vector_store_path = "vector_store/faiss_bge_m3_kwc_code"

    embedding_model = init_embedding_model(URL, API_KEY, MODEL_NAME)

    init_doc_vector_store(embedding_model, doc_dir, doc_vector_store_path)
    init_code_vector_store(embedding_model, code_dir, code_vector_store_path)
    # 启动服务
    mcp.run(transport="sse", host="0.0.0.0", port=8003)
