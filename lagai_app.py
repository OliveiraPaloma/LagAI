import streamlit as st
 import pandas as pd
 import google.generativeai as genai
 

 # Configuração da página
 st.set_page_config(page_title="LagAI", page_icon="🎮", layout="wide")
 

 # --- Inicialização do Gemini ---
 def inicializar_gemini():
  genai.configure(api_key=st.secrets["GEMINI_API_KEY"]) # Carrega a chave da API do arquivo secrets.toml
  return genai.GenerativeModel('gemini-pro') # Retorna o modelo Gemini
 

 # --- Função de Busca ---
 def buscar_jogos(consulta, modelo):
  """
  Busca informações sobre jogos online usando o Gemini.
 

  Args:
  consulta (str): A pergunta do usuário.
  modelo: A instância do modelo Gemini GenerativeModel.
 

  Returns:
  str: Os resultados da busca do Gemini.
  """
  try:
  prompt = f"Encontre informações detalhadas sobre jogos online relacionados a: {consulta}. Inclua detalhes como cross-play, data de lançamento, avaliações, plataformas e preços."
  resposta = modelo.generate_content(prompt)
  return resposta.text
  except Exception as e:
  st.error(f"Ocorreu um erro durante a busca: {e}")
  return None
 

 # --- Dados de Cross-Play (Exemplo) ---
 def carregar_dados_crossplay():
  """
  Carrega ou define dados sobre compatibilidade cross-play.
  Em um aplicativo real, isso viria de um banco de dados ou API.
 

  Returns:
  pd.DataFrame: Um DataFrame com informações de cross-play.
  """
  dados = {
  "Jogo": ["Fortnite", "Rocket League", "Minecraft"],
  "Plataformas": ["PC, PS, Xbox, Switch, Mobile", "PC, PS, Xbox, Switch", "PC, PS, Xbox, Switch, Mobile"],
  "Cross-Play": ["Sim", "Sim", "Sim"]
  }
  return pd.DataFrame(dados)
 

 # --- Função Principal do Aplicativo ---
 def principal():
  st.title("LagAI - Seu Centro de Informações de Jogos 🎮")
 

  # Inicializa o modelo Gemini
  modelo_gemini = inicializar_gemini()
 

  # Barra lateral de navegação
  with st.sidebar:
  st.header("Navegação")
  pagina_selecionada = st.radio("Escolha uma seção", ["Início", "Buscar Jogo", "Guia de Cross-Play", "Sobre"])
 

  # Página Inicial
  if pagina_selecionada == "Início":
  st.header("Bem-vindo ao LagAI!")
  st.write("Sua fonte para informações completas sobre jogos online.")
 

  # Página de Busca de Jogos
  elif pagina_selecionada == "Buscar Jogo":
  st.header("Buscar Informações de Jogo")
  termo_de_busca = st.text_input("Digite o título do jogo ou a consulta de busca:")
  if st.button("Buscar"):
  if termo_de_busca:
  with st.spinner("Buscando..."):
  resultados_da_busca = buscar_jogos(termo_de_busca, modelo_gemini)
  if resultados_da_busca:
  st.subheader("Resultados da Busca")
  st.markdown(resultados_da_busca, unsafe_allow_html=True)
  else:
  st.info("Nenhum resultado encontrado. Por favor, tente uma busca diferente.")
  else:
  st.warning("Por favor, digite um termo de busca.")
 

  # Página do Guia de Cross-Play
  elif pagina_selecionada == "Guia de Cross-Play":
  st.header("Compatibilidade Cross-Play")
  dataframe_crossplay = carregar_dados_crossplay()
  st.dataframe(dataframe_crossplay)
 

  # Página Sobre
  elif pagina_selecionada == "Sobre":
  st.header("Sobre o LagAI")
  st.write("LagAI foi projetado para fornecer aos jogadores informações detalhadas sobre jogos online, com foco em capacidades cross-play.")
 

 if __name__ == "__main__":
  principal()
