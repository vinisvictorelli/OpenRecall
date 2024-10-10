# Usar uma imagem base oficial do Python
FROM python:3.12-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos necessários para o contêiner
COPY . /app

# Atualizar o apt-get e instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    curl \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependências Python, incluindo Streamlit
RUN pip install --no-cache-dir -r requirements.txt

# Baixar o modelo minicpm-v para uso local
RUN ollama serve & sleep 5 && ollama pull minicpm-v

# Expor a porta padrão do Streamlit
EXPOSE 8501

# Definir o comando de entrada padrão para iniciar o Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
