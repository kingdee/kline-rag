from typing import List, Tuple
from sentence_transformers import CrossEncoder
from langchain_core.documents import Document


class CrossEncoderReranker:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2", device: str = "cpu"):
        self.model_name = model_name
        self.device = device
        self.model = CrossEncoder(model_name, device=device)


    def rerank(self, query: str, candidates: List[Document]) -> List[Tuple[Document, float]]:
        pairs = [(query, c.page_content) for c in candidates]
        scores = self.model.predict(pairs)
        scored = list(zip(candidates, scores))
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored