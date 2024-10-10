# Freecall

Freecall é uma aplicação inteligente para captura de tela e geração de descrições, projetada para fornecer um histórico visual detalhado das suas atividades diárias, enquanto preserva sua privacidade ao rodar localmente. Esta aplicação utiliza o modelo multimodal **Minicpm-v** para gerar descrições de imagens capturadas automaticamente.

## Funcionalidades

- **Captura de Tela Automática**: Tira capturas de tela periodicamente e as salva em uma pasta local.
- **Geração de Descrições de Imagens**: Utiliza o modelo **Minicpm-v** para criar descrições detalhadas de cada captura de tela.
- **Pesquisa Eficiente**: Um mecanismo de busca que permite encontrar rapidamente imagens e suas descrições a partir de palavras-chave.
- **Privacidade Garantida**: Todo o processamento é feito localmente, sem necessidade de enviar dados para servidores externos.

## Como Usar

### 1. Capturar Screenshots
Ao clicar em "Capturar Tela", a ferramenta começa a tirar automaticamente capturas de tela, que são salvas na pasta `capture` dentro do diretório da aplicação.

### 2. Descrever Imagens
Quando terminar de capturar, basta clicar em "Descrever Imagens" para que as capturas sejam processadas e descritas pelo modelo **Minicpm-v**.

### 3. Pesquisar Histórico
Use o mecanismo de pesquisa embutido para encontrar informações e imagens anteriores utilizando suas próprias palavras.

## Como Rodar o Projeto

### 1. Pré-requisitos

- **Python 3.9** ou superior.
- **Ollama** para o gerenciamento do modelo **Minicpm-v**.
- **Streamlit** para rodar a aplicação web.

### 2. Instalando as Dependências

Clone o repositório e instale as dependências do projeto.

```bash
git clone https://github.com/usuario/freecall.git
cd freecall
pip install -r requirements.txt
