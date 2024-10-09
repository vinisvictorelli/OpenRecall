import chromadb
from chromadb.utils import embedding_functions
import pandas as pd
import uuid

def create_vector_database(query):
    df = pd.read_parquet('data/data.parquet')
    # Carrega os dados 
    documents = [i for i in df['description']]
    metadatas = [{'file_path': i} for i in df['filepath']]
    ids = [str(uuid.uuid4()) for i in df['description']]

    # Instancia um cliente do ChromaDB. Os dados serão armazenados em disco (uma pasta chamada 'vector_db_recall' será criada no mesmo diretório deste arquivo).
    chroma_client = chromadb.PersistentClient(path="vector_db_recall")

    # Seleciona o modelo de embeddings a ser utilizado.
    # A lista de nomes de modelos pode ser encontrada aqui: https://www.sbert.net/docs/pretrained_models.html
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

    # Use esta linha para deletar o banco de dados
    # chroma_client.delete_collection(name="my_collection")

    # Cria a coleção, ou seja, o banco de dados vetorial. Caso já exista, ele será reutilizado. Especificamos o modelo que queremos usar para gerar os embeddings.
    collection = chroma_client.get_or_create_collection(name="vector_data", embedding_function=sentence_transformer_ef)

    # Adiciona todos os dados ao banco de dados vetorial. O ChromaDB converte e armazena automaticamente o texto como embeddings vetoriais. Isso pode levar alguns minutos.
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    # Faz uma consulta no banco de dados vetorial, retornando os 3 resultados mais próximos com base no texto da consulta.
    results = collection.query(
        query_texts=[query],
        n_results=3,
        include=['documents', 'distances', 'metadatas']
    )

    return results['documents'], results['metadatas']
