from typing import List
import os
import fitz  # PyMuPDF
# from langchain.schema import Document
from langchain_core.documents import Document
# from langchain.text_splitter import MarkdownHeaderTextSplitter
from langchain_text_splitters.markdown import MarkdownHeaderTextSplitter

def chunk_markdown_by_headers(md_path: str) -> List[Document]:
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


def chunk_markdown_by_folder(md_dir: str) -> List[Document]:
    docs: List[Document] = []
    chunk_index = 0

    # 支持的文件类型
    supported_exts = [".md", ".pdf"]

    for root, _, files in os.walk(md_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext not in supported_exts:
                continue

            file_path = os.path.join(root, file)

            try:
                if ext == ".md":
                    # 读取 Markdown 文件
                    with open(file_path, "r", encoding="utf-8") as f:
                        text = f.read()

                elif ext == ".pdf":
                    # 使用 PyMuPDF 提取 PDF 文本
                    text = ""
                    with fitz.open(file_path) as pdf:
                        for page in pdf:
                            text += page.get_text("text")

            except Exception as e:
                print(f"⚠️ 无法读取文件 {file_path}: {e}")
                continue

            # 创建 Document
            doc = Document(
                page_content=text or "",
                metadata={
                    "source": os.path.relpath(file_path, md_dir),
                    "chunk_index": chunk_index
                }
            )
            docs.append(doc)
            chunk_index += 1

    return docs
