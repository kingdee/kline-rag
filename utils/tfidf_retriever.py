from typing import List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from langchain_core.documents import Document


class SimpleTfidfRetriever:
    def __init__(self, max_features: int = 50000, ngram_range=(1, 2)):
        self.vec = TfidfVectorizer(ngram_range=ngram_range, max_features=max_features)
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