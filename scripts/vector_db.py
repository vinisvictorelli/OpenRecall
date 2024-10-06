
import chromadb
from chromadb.utils import embedding_functions
import pandas as pd
import uuid

def create_vector_database(query):
    df = pd.read_parquet('data/data.parquet')
    # Load sample data (a restaurant menu of items)
    documents = [i for i in df['description']]
    metadatas = [{'file_path': i} for i in df['filepath']]
    ids = [str(uuid.uuid4()) for i in df['description']]

    # Instantiate chromadb instance. Data is stored on disk (a folder named 'my_vectordb' will be created in the same folder as this file).
    chroma_client = chromadb.PersistentClient(path="vector_db_recall")

    # Select the embedding model to use.
    # List of model names can be found here https://www.sbert.net/docs/pretrained_models.html
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

    # Use this to delete the database
    # chroma_client.delete_collection(name="my_collection")

    # Create the collection, aka vector database. Or, if database already exist, then use it. Specify the model that we want to use to do the embedding.
    collection = chroma_client.get_or_create_collection(name="vector_data", embedding_function=sentence_transformer_ef)

    # Add all the data to the vector database. ChromaDB automatically converts and stores the text as vector embeddings. This may take a few minutes.
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    results = collection.query(
        query_texts=[query],
        n_results=1,
        include=['documents', 'distances', 'metadatas']
    )

    return results['documents'],results['metadatas']

