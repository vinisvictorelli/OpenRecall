from PIL import Image
import ollama
import os
import pandas as pd

def generate_description(instruction, file_path):
    result = ollama.generate(
        model='minicpm-v',
        prompt=instruction,
        images=[file_path],
        stream=False
    )['response']
    
    return result

instruction = "From the image, extract what the USER is doing with the most information that you can get, include URL if applicable."
file_path = 'capture'
def create_database():
    # Path to the Parquet file
    parquet_file_path = 'data/data.parquet'

    # Check if the Parquet file already exists
    if os.path.exists(parquet_file_path):
        # Load the existing Parquet file
        data = pd.read_parquet(parquet_file_path)
    else:
        # If it doesn't exist, create an empty DataFrame
        data = pd.DataFrame({
        'filepath': [],
        'description': []
        })
    for file in os.listdir(file_path):
        if "._" not in file:
            new_data = pd.DataFrame({
                'filepath': [f'{file_path}/{file}'],
                'description': [generate_description(instruction,f'{file_path}/{file}')]
            })
            print(f'New file created with description')
            print(new_data)
            data = pd.concat([data, new_data], ignore_index=True)
    print('Finished')

    data.to_parquet(parquet_file_path)

def debug():
    data = pd.read_parquet('../data/data.parquet')
    print(data)

