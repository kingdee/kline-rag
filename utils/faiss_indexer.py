import os
from typing import List, Optional
import numpy as np
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.documents import Document
from langchain.embeddings.base import Embeddings


class FaissIndexer:
    def __init__(self, emb: Embeddings):
        self.emb = emb
        self.store: Optional[FAISS] = None

    def build_from_documents(self, docs: List[Document], save_path: Optional[str] = None) -> FAISS:
        # 使用 LangChain 的封装（会调用 embeddings）
        self.store = FAISS.from_documents(docs, self.emb)
        if save_path:
            os.makedirs(save_path, exist_ok=True)
            self.store.save_local(save_path)
        return self.store

    def load(self, path: str) -> FAISS:
        self.store = FAISS.load_local(path, self.emb, allow_dangerous_deserialization=True)
        return self.store

    def get_store(self) -> FAISS:
        assert self.store is not None, "FAISS store not yet built or loaded"
        return self.store