import streamlit as st
 import pandas as pd
 import google.generativeai as genai
 import os
 

 # Configurar a API Gemini
 genai.configure(api_key=os.environ['GEMINI_API_KEY'])
 model = genai.GenerativeModel('gemini-pro')
 

 st.set_page_config(page_title="LagAI com Gemini", layout="wide")
 

 def buscar_jogos_online_gemini(pergunta):
  try:
  prompt_parts = [
  f"Responda à seguinte pergunta sobre jogos online, buscando informações relevantes na web:\n\n{pergunta}\n\nListe os principais resultados encontrados e seus respectivos links, se disponíveis. Se não encontrar resultados relevantes, informe claramente."
  ]
  response = model.generate_content(prompt_parts)
  response.resolve() # Espera a resposta ser completamente gerada
 

  if response.text:
  return response.text
  else:
  return "Não encontrei resultados relevantes. 😢"
  except Exception as e:
  print(f"Ocorreu um erro ao buscar com a Gemini API: {e}")
  return "Ocorreu um erro na busca. 😢"
 

 def criar_dataframe_crossplay():
  dados = {
  "Jogo": [
  "Minecraft", "Pokémon UNITE", "Fortnite",
  "Call of Duty: Warzone", "APEX Legends",
  "Call of Duty: Black Ops 6", "Rocket League",
  "Ghostbusters: Spirits Unleashed", "Battlefield 2042",
  "Among Us", "Warframe", "Fortnite"
  ],
  "Plataformas": [
  "Várias", "Várias", "Várias",
  "Várias", "Várias", "Várias", "Várias",
  "Várias", "Várias", "Várias", "Várias", "Várias"
  ]  # Substitua "Várias" pelas plataformas específicas de cada jogo
  }
  return pd.DataFrame(dados)
 

 # --- Interface ---
 st.sidebar.title("🎮 LagAI Menu")
 page = st.sidebar.radio("Navegação", ["Início", "Busca com IA", "Guias Cross-Play", "Sobre"])
 

 if page == "Início":
  st.title("🎮 Bem-vindo ao LagAI!")
  st.write("Explore o universo dos jogos cross-play com a Gemini!")
 

 elif page == "Busca com IA":
  st.title("🔍 Pesquise sobre jogos (com Gemini)")
  consulta = st.text_input("Digite o que você quer saber:")
  if st.button("Buscar"):
  with st.spinner("Consultando a IA..."):
  resultado = buscar_jogos_online_gemini(consulta)
  st.markdown("### Resultado:")
  st.markdown(resultado, unsafe_allow_html=True)
 

 elif page == "Guias Cross-Play":
  st.header("🕹️ Jogos com suporte a Cross-Play")
  df_crossplay = criar_dataframe_crossplay()
  st.table(df_crossplay)
 

 elif page == "Sobre":
  st.header("👾 Sobre o LagAI")
  st.write("Este app usa a Gemini API para trazer informações sobre jogos! Criado por uma gamer raiz 🕹️❤️")
