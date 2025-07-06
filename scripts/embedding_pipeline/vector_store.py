import os
import pandas as pd
from chromadb.config import Settings
import chromadb
from chromadb.utils import embedding_functions


class VectorStoreChroma:
    def __init__(self, persist_directory="vector_store/chromadb", embedding_function=None):
        self.persist_directory = persist_directory
        self.embedding_function = embedding_function

        self.client = chromadb.Client(Settings(
            persist_directory=self.persist_directory,
            chroma_db_impl="duckdb+parquet"
        ))

        existing_collections = [col.name for col in self.client.list_collections()]
        if "complaints_collection" in existing_collections:
            self.collection = self.client.get_collection("complaints_collection")
        else:
            ef = embedding_function or embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name="models/all-MiniLM-L6-v2-local"  # Local model path
            )
            self.collection = self.client.create_collection(
                name="complaints_collection",
                embedding_function=ef
            )

    def add_documents(self, texts, metadatas=None, ids=None):
        self.collection.add(documents=texts, metadatas=metadatas, ids=ids)

    def query(self, query_text, n_results=5):
        return self.collection.query(query_texts=[query_text], n_results=n_results)

    def persist(self):
        self.client.persist()

    def reset(self):
        self.collection.delete(where={})


def batch_add_documents(store, texts, metadatas, ids, batch_size=500):
    total = len(texts)
    for start_idx in range(0, total, batch_size):
        end_idx = min(start_idx + batch_size, total)
        batch_texts = texts[start_idx:end_idx]
        batch_metas = metadatas[start_idx:end_idx]
        batch_ids = ids[start_idx:end_idx]

        print(f"Adding batch {start_idx} to {end_idx} of {total}...")
        store.add_documents(batch_texts, metadatas=batch_metas, ids=batch_ids)


if __name__ == "__main__":
    from scripts.embedding_pipeline.embedding import load_embedding_model, embed_texts
    from scripts.embedding_pipeline.chunking import chunk_texts

    # Load data
    df = pd.read_csv("Data/processed/filtered_complaints.csv")

    #  Sample data for faster testing
    df = df.sample(n=1000, random_state=42)

    texts = df["Cleaned Narrative"].tolist()
    chunks = chunk_texts(texts)

    chunk_texts_only = [chunk["text"] for chunk in chunks]
    metadatas = [{"source_index": chunk["source_index"]} for chunk in chunks]
    ids = [str(i) for i in range(len(chunks))]

    # Load local embedding model
    model = load_embedding_model(model_path="models/all-MiniLM-L6-v2-local")
    embeddings = embed_texts(model, chunk_texts_only)

    store = VectorStoreChroma(persist_directory="vector_store/chromadb")

    # Add in batches (adjust size as needed)
    batch_add_documents(store, chunk_texts_only, metadatas, ids, batch_size=500)

    store.persist()
    print("✅ Vector store saved.")
