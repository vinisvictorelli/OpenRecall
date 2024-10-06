import streamlit as st
from scripts.vector_db import create_vector_database
from scripts.capture_screenshot import main_screenshot_function
from scripts.description import create_database

# Função para exibir os resultados
def display_results(query):
    show_search()
    result, metadata = create_vector_database(query)
    
    file_paths = [d['file_path'] for sublist in metadata for d in sublist]
    print(file_paths)
    results = [d for sublist in result for d in sublist]
    
    result_str = ""
    
    if result:
        # Exibir imagens e descrições
        for i, doc in enumerate(results):
            if i < len(file_paths):
                image_url = file_paths[i]
                
                # Exibir imagem e descrição no Streamlit
                st.image(image_url, caption=f"Resultado {i+1}", use_column_width=True)
                st.write(f"**Descrição:** {doc}")
    else:
        st.write("Nenhum resultado encontrado.")

def home():
    st.markdown("""
    # Freecall
    Bem-vindo ao Freecall, a ferramenta que facilita o acompanhamento das suas atividades diárias. 
    Capture e busque informações visuais de maneira eficiente e segura, sem comprometer a sua privacidade.
    """)
# Função para mostrar a página de busca
def show_search():
    st.text_input("## Pesquisar usando suas palavras", key="search_input", on_change=search_query)

# Função para processar a consulta
def search_query():
    query = st.session_state.search_input
    print(query)
    display_results(query)

# Função para mostrar a página em branco
def record_images():
    st.markdown('''
    # Captura de Tela com Descrição Inteligente
    Esta página permite que você capture imagens da sua tela e as envie para uma inteligência artificial avançada (LLM) que irá gerar descrições detalhadas das capturas. O objetivo é ajudar você a lembrar ou organizar informações de maneira prática e eficiente.\n
    ## Como Funciona:\n
    Captura de Tela: Basta clicar em 'Capturar tela' para começar a capturar screenshots.\n
    Envio para a LLM: As imagens capturadas são enviadas para uma LLM. A LLM processa a imagem e gera uma descrição detalhada.\n
    ''')

    capturar_tela = st.button('Capturar tela',on_click=main_screenshot_function)
    descrever_imagens = st.button('Descrever as imagens',on_click=create_database)

# Função principal para gerenciar a interface Streamlit
def main():
    st.sidebar.title("Opções")
    st.sidebar.button("Home",on_click=home)
    st.sidebar.button("Capturar Screenshots",on_click=record_images)
    st.sidebar.button("Mecanismo de Pesquisa",on_click=show_search)
    
# Executar Streamlit diretamente
if __name__ == "__main__":
    main()
