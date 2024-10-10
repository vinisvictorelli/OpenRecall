# Freecall

Freecall é uma tentativa de recriar as funcionalidades do software Recall apresentado pela Microsoft. Onde a ferramenta cria um histórico visual do usuário e permite através do uso de LLM's, a pesquisa por esse histórico usando uma descrição feita pelo próprio usuário. A grande diferença é que o freecall roda inteiramente local, sem o risco de enviar suas informações para servidores externos.

**DISCLAIMER: A ferramenta é apenas uma maneira que eu pensei para estudar mais sobre os usos que LLM's podem ter no nosso dia a dia. Então não é recomendável o uso dela como uma forma de backup para informações importantes**

## Funcionalidades

- **Captura de Tela Automática**: Tira capturas de tela usando uma ánalise dos pixels da tela do usuário e as salva em uma pasta local (pasta 'capture' que se encontra na raiz do projeto).
- **Geração de Descrições de Imagens**: Utiliza o modelo **Minicpm-v** para criar descrições detalhadas de cada captura de tela.
- **Pesquisa Eficiente**: Um mecanismo de busca que permite encontrar rapidamente imagens e suas descrições a partir das suas palavras.
- **Privacidade**: Todo o processamento é feito localmente, sem necessidade de enviar dados para servidores externos.

## Como Usar

### 1. Capturar Screenshots
Ao clicar em "Capturar Tela", a ferramenta começa a tirar automaticamente capturas de tela, que são salvas na pasta `capture` dentro do diretório da aplicação.

### 2. Descrever Imagens
Quando terminar de capturar, basta clicar em "Descrever Imagens" para que as capturas sejam processadas e descritas pelo modelo **Minicpm-v**.

### 3. Pesquisar Histórico
Use o mecanismo de pesquisa embutido para encontrar informações e imagens anteriores utilizando suas próprias palavras.

## Como Rodar o Projeto

### 1. Pré-requisitos

- **Python 3.12** ou superior.
- **Ollama** para o gerenciamento do modelo **Minicpm-v**.
- **Streamlit** para rodar a aplicação web.

### 2. Instalando as Dependências

Clone o repositório e instale as dependências do projeto.

```bash
git clone https://github.com/usuario/freecall.git
cd freecall
pip install -r requirements.txt
```
### 3. Configurando o Ollama

Certifique-se de ter o Ollama instalado corretamente. Caso não tenha, você pode instalar utilizando o comando abaixo:

```bash
curl -sSfL https://ollama.com/download.sh | sh
```

Após instalar o Ollama, baixe o modelo Minicpm-v:

```bash
ollama pull minicpm-v
```

### 4. Executando a Aplicação

Execute a aplicação utilizando o Streamlit:
```bash
streamlit run app.py
```

### Próximos Passos
Ainda há espaço para várias melhorias incluindo:
- [ ] Rodar a aplicação inteiramente em um container Docker, facilitando a execução da mesma.
- [ ] Melhorar a performance para descrever as imagens, **ainda extremamente lento**
### Contribuindo

Sinta-se à vontade para abrir um pull request ou relatar problemas na seção Issues.