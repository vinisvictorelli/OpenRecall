import chromadb
from chromadb.utils import embedding_functions
import pandas as pd
import uuid

def create_vector_database():
    df = pd.read_parquet('data/data.parquet')
    # Load the data
    documents = [i for i in df['description']]
    metadatas = [{'file_path': i} for i in df['filepath']]
    ids = [str(uuid.uuid4()) for i in df['description']]

    # Instantiate a ChromaDB client. The data will be stored on disk (a folder called 'vector_db_recall' will be created in the same directory as this file).
    chroma_client = chromadb.PersistentClient(path="vector_db_recall")

    # Select the embedding model to be used.
    # The list of model names can be found here: https://www.sbert.net/docs/pretrained_models.html
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

    # Use this line to delete the database
    # chroma_client.delete_collection(name="my_collection")

    # Create the collection, i.e., the vector database. If it already exists, it will be reused. We specify the model we want to use to generate the embeddings.
    collection = chroma_client.get_or_create_collection(name="vector_data", embedding_function=sentence_transformer_ef)

    # Add all data to the vector database. ChromaDB automatically converts and stores the text as vector embeddings. This may take a few minutes.
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

def search_vector_database(query):
    # Instantiate a ChromaDB client. The data will be stored on disk (a folder called 'vector_db_recall' will be created in the same directory as this file).
    chroma_client = chromadb.PersistentClient(path="vector_db_recall")

    # Select the embedding model to be used.
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

    # Create the collection, i.e., the vector database. If it already exists, it will be reused. We specify the model we want to use to generate the embeddings.
    collection = chroma_client.get_or_create_collection(name="vector_data", embedding_function=sentence_transformer_ef)

    # Perform a query on the vector database, returning the 3 closest results based on the query text.
    results = collection.query(
        query_texts=[query],
        n_results=3,
        include=['documents', 'distances', 'metadatas']
    )

    return results['documents'], results['metadatas']
