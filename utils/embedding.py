from typing import List
import requests
from langchain.embeddings.base import Embeddings


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