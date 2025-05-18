import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

# Configurar a API Gemini
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Central do Jogador", layout="wide")

def buscar_info_jogo_online(nome_jogo):
    try:
        prompt = f"Busque informações detalhadas online sobre o jogo '{nome_jogo}'. Inclua detalhes sobre:\n- Suporte a cross-play (sim ou não e em quais plataformas)\n- Data de lançamento\n- Avaliações (de diferentes fontes, se possível)\n- Plataformas em que o jogo está disponível\n- Valor do jogo (preço base ou se é gratuito com compras)\n\nFormate a resposta de forma clara e concisa."
        response = model.generate_content(prompt)
        response.resolve()
        if response.text:
            return response.text
        else:
            return f"Não encontrei informações detalhadas online sobre '{nome_jogo}'."
    except Exception as e:
        print(f"Ocorreu um erro ao buscar informações online com a Gemini API: {e}")
        return f"Ocorreu um erro ao buscar informações sobre '{nome_jogo}'."

def identificar_jogo_com_gemini(pergunta):
    try:
        prompt = f"O usuário está perguntando sobre um jogo online com a seguinte frase: '{pergunta}'. Qual é o nome exato desse jogo? Se for possível identificar um jogo específico, responda apenas com o nome do jogo. Se não for possível identificar um jogo claramente, diga 'Não identificado'."
        response = model.generate_content(prompt)
        response.resolve()
        if response.text and response.text != "Não identificado":
            return response.text.strip()
        else:
            return None
    except Exception as e:
        print(f"Erro ao identificar o jogo com Gemini: {e}")
        return None

# --- Interface ---
st.sidebar.title("🎮 Painel Gamer")
page = st.sidebar.radio("Navegação", ["Início", "Buscar Jogo", "Sobre"])

if page == "Início":
    st.title("Bem-vindo Jogador!")
    st.write("Encontre informações detalhadas sobre seus jogos online favoritos.")

elif page == "Buscar Jogo":
    st.title("🔍 Buscar Informações de Jogo")
    consulta = st.text_input("Digite o nome do jogo que você procura:")
    if st.button("Buscar"):
        with st.spinner("Buscando informações..."):
            nome_do_jogo = identificar_jogo_com_gemini(consulta)
            if nome_do_jogo:
                info_jogo = buscar_info_jogo_online(nome_do_jogo)
                st.subheader(f"Informações sobre: {nome_do_jogo}")
                st.markdown(info_jogo, unsafe_allow_html=True)
            else:
                st.info("Não foi possível identificar um jogo específico na sua busca. Por favor, seja mais específico.")

elif page == "Guias Cross-Play": # Mantive a página de guias como estava
    st.header("🕹️ Jogos com suporte a Cross-Play")
    st.table(pd.DataFrame({
        "Jogo": ["Fortnite", "Rocket League"],
        "Plataformas": ["PC, PS, Xbox", "PC, PS, Xbox, Switch"]
    }))

elif page == "Sobre":
    st.header("👾 Sobre a Central do Jogador")
    st.write("Um espaço para jogadores encontrarem informações importantes sobre seus jogos online.")
