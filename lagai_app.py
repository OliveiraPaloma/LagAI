import streamlit as st
import pandas as pd
import google.generativeai as genai

st.set_page_config(page_title="LagAI com Gemini", layout="wide")

# --- Gemini API ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def buscar_jogos_online(pergunta):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(pergunta)
    return response.text

# --- Interface ---
st.sidebar.title("LagAI Menu")
page = st.sidebar.radio("Navegação", ["Início", "Busca com IA", "Guias Cross-Play", "Sobre"])

if page == "Início":
    st.title("🎮 Bem-vindo ao LagAI!")
    st.write("Explore o universo dos jogos cross-play!")

elif page == "Busca com IA":
    st.title("🔍 Pesquise sobre jogos com IA (Google Gemini)")
    consulta = st.text_input("Digite o que você quer saber:")
    if st.button("Buscar"):
        with st.spinner("Consultando IA..."):
            resultado = buscar_jogos_online(consulta)
            st.markdown("### Resultado:")
            st.write(resultado)

elif page == "Guias Cross-Play":
    st.header("🕹️ Jogos com suporte a Cross-Play")
    st.table(pd.DataFrame({
        "Jogo": ["Fortnite", "Rocket League"],
        "Plataformas": ["PC, PS, Xbox", "PC, PS, Xbox, Switch"]
    }))

elif page == "Sobre":
    st.header("👾 Sobre o LagAI")
    st.write("Esse site usa a IA Gemini para trazer respostas inteligentes sobre o mundo dos jogos!")
import streamlit as st
import pandas as pd
import google.generativeai as genai

st.set_page_config(page_title="LagAI com Gemini", layout="wide")

# --- Gemini API ---
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def buscar_jogos_online(pergunta):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(pergunta)
    return response.text

# --- Interface ---
st.sidebar.title("LagAI Menu")
page = st.sidebar.radio("Navegação", ["Início", "Busca com IA", "Guias Cross-Play", "Sobre"])

if page == "Início":
    st.title("🎮 Bem-vindo ao LagAI!")
    st.write("Explore o universo dos jogos cross-play!")

elif page == "Busca com IA":
    st.title("🔍 Pesquise sobre jogos com IA (Google Gemini)")
    consulta = st.text_input("Digite o que você quer saber:")
    if st.button("Buscar"):
        with st.spinner("Consultando IA..."):
            resultado = buscar_jogos_online(consulta)
            st.markdown("### Resultado:")
            st.write(resultado)

elif page == "Guias Cross-Play":
    st.header("🕹️ Jogos com suporte a Cross-Play")
    st.table(pd.DataFrame({
        "Jogo": ["Fortnite", "Rocket League"],
        "Plataformas": ["PC, PS, Xbox", "PC, PS, Xbox, Switch"]
    }))

elif page == "Sobre":
    st.header("👾 Sobre o LagAI")
    st.write("Esse site usa a IA Gemini para trazer respostas inteligentes sobre o mundo dos jogos!")
