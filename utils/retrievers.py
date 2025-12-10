from typing import List
# from langchain.retrievers import EnsembleRetriever, MultiQueryRetriever
# from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers.ensemble import EnsembleRetriever
from langchain_classic.retrievers.multi_query import MultiQueryRetriever

from langchain_community.vectorstores import FAISS

from .tfidf_retriever import SimpleTfidfRetriever




class RetrieverFactory:
    @staticmethod
    def similarity(faiss_store: FAISS, k: int = 5):
        return faiss_store.as_retriever(search_type="similarity", search_kwargs={"k": k})


    @staticmethod
    def mmr(faiss_store: FAISS, k: int = 5, fetch_k: int = 20):
        return faiss_store.as_retriever(search_type="mmr", search_kwargs={"k": k, "fetch_k": fetch_k})


    @staticmethod
    def ensemble_hybrid(faiss_store: FAISS, tfidf: SimpleTfidfRetriever, k: int = 5):
        class TfidfWrapper:
            def __init__(self, tfidf):
                self._tfidf = tfidf
            def get_relevant_documents(self, query, k=5):
                return self._tfidf.get_relevant_documents(query, k=k)


        dense = faiss_store.as_retriever(search_type="similarity", search_kwargs={"k": k})
        sparse = TfidfWrapper(tfidf)
        return EnsembleRetriever(retrievers=[dense, sparse], weights=[0.6, 0.4])


    @staticmethod
    def multquery(faiss_store: FAISS, llm, k: int = 5):
        """
        args:
            k: k_per_query
        """
        base = faiss_store.as_retriever(search_type="similarity", search_kwargs={"k": k})
        return MultiQueryRetriever.from_llm(llm=llm, retriever=base)