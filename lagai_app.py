import streamlit as st
import pandas as pd
import requests
import os
import json  # Importe a biblioteca json para formatar a saída

st.set_page_config(page_title="LagAI com Google Search", layout="wide")

# Função para buscar via API do SerpAPI
def buscar_jogos_online(pergunta):
    api_key = st.secrets["GEMINI_API_KEY"]
    url = "https://serpapi.com/search"
    params = {
        "q": pergunta,
        "engine": "google",
        "api_key": api_key,
        "num": 10
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lança uma exceção para erros HTTP (status code diferente de 200)
        data = response.json()
        print("Resposta bruta da SerpAPI:")
        print(json.dumps(data, indent=4, ensure_ascii=False))  # Imprime a resposta formatada

        if "organic_results" in data:
            resultados = data["organic_results"]
            texto = "\n\n".join([f"🔗 [{res['title']}]({res['link']})\n{res.get('snippet', '')}" for res in resultados])
        else:
            texto = "Não encontrei nada. 😢"
        return texto
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a SerpAPI: {e}")
        return "Ocorreu um erro ao buscar os resultados. 😢"

# --- Interface ---
st.sidebar.title("🎮 LagAI Menu")
page = st.sidebar.radio("Navegação", ["Início", "Busca com IA", "Guias Cross-Play", "Sobre"])

if page == "Início":
    st.title("🎮 Bem-vindo ao LagAI!")
    st.write("Explore o universo dos jogos cross-play!")

elif page == "Busca com IA":
    st.title("🔍 Pesquise sobre jogos (com Google Search)")
    consulta = st.text_input("Digite o que você quer saber:")
    if st.button("Buscar"):
        with st.spinner("Consultando a internet..."):
            resultado = buscar_jogos_online(consulta)
            st.markdown("### Resultado:")
            st.markdown(resultado, unsafe_allow_html=True)

elif page == "Guias Cross-Play":
    st.header("🕹️ Jogos com suporte a Cross-Play")
    st.table(pd.DataFrame({
        "Jogo": ["Fortnite", "Rocket League"],
        "Plataformas": ["PC, PS, Xbox", "PC, PS, Xbox, Switch"]
    }))

elif page == "Sobre":
    st.header("👾 Sobre o LagAI")
    st.write("Esse app usa a API do Google via SerpAPI para trazer resultados rápidos sobre jogos! Criado por uma gamer raiz 🕹️❤️")
