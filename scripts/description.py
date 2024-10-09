from PIL import Image
import ollama
import os
import pandas as pd

# Gera a descrição das imagens usando o modelo minicpm-v
# Você pode verificar os outros modelos da ollama no link: https://ollama.com/library
def generate_description(instruction, file_path):
    result = ollama.generate(
        model='minicpm-v',
        prompt=instruction,
        images=[file_path],
        stream=False
    )['response']
    
    return result

instruction = "A partir da imagem, extraia o que o USUÁRIO está fazendo com o máximo de informações que você puder obter, incluindo URL, se aplicável."
file_path = 'capture'

def create_database():
    # Caminho para o arquivo Parquet
    parquet_file_path = 'data/data.parquet'

    # Verifica se o arquivo Parquet já existe
    if os.path.exists(parquet_file_path):
        # Carrega o arquivo Parquet existente
        data = pd.read_parquet(parquet_file_path)
    else:
        # Se não existir, cria um DataFrame vazio
        data = pd.DataFrame({
        'filepath': [],
        'description': []
        })
    
    for file in os.listdir(file_path):
        if "._" not in file:
            new_data = pd.DataFrame({
                'filepath': [f'{file_path}/{file}'],
                'description': [generate_description(instruction, f'{file_path}/{file}')]
            })
            print(f'Novo arquivo criado com descrição')
            print(new_data)
            data = pd.concat([data, new_data], ignore_index=True)
    print('Concluído')

    # Salva os dados no formato Parquet
    data.to_parquet(parquet_file_path)

def debug():
    # Debuga o código e ver se os dados estão sendo carregados de maneira correta
    data = pd.read_parquet('../data/data.parquet')
    print(data)
