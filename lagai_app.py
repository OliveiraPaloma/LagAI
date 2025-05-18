import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

 #Configuração da página
 st.set_page_config(page_title="LagAI",page_icon="🎮",layout="wide")
 

 #Inicialização do Gemini
 def inicializar_gemini():
  genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
  return genai.GenerativeModel("gemini-pro")
 

 #Função de Busca
 def buscar_jogos(consulta,modelo):
  try:
  prompt=f"Encontre informações detalhadas sobre jogos online relacionados a:{consulta}.Inclua detalhes como cross-play,data de lançamento,avaliações,plataformasepreços."
  resposta=modelo.generate_content(prompt)
  return resposta.text
  except Exception as e:
  st.error(f"Ocorreu um erro na busca:{e}")
  return None
 

 #Dados de Cross-Play (Exemplo)
 def carregar_dados_crossplay():
  dados={
  "Jogo":["Fortnite","Rocket League","Minecraft"],
  "Plataformas":["PC,PS,Xbox,Switch,Mobile","PC,PS,Xbox,Switch","PC,PS,Xbox,Switch,Mobile"],
  "Cross-Play":["Sim","Sim","Sim"]
  }
  return pd.DataFrame(dados)
 

 #Função Principal
 def principal():
  st.title("LagAI-Seu Centro de Informações de Jogos🎮")
 

  #Inicializa Gemini
  modelo_gemini=inicializar_gemini()
 

  #Barra de navegação
  with st.sidebar:
  st.header("Navegação")
  pagina_selecionada=st.radio("Escolha uma seção",["Início","Buscar Jogo","Guia de Cross-Play","Sobre"])
 

  #Página Inicial
  if pagina_selecionada=="Início":
  st.header("Bem-vindo ao LagAI!")
  st.write("Sua fonte para informações completas sobre jogos online.")
 

  #Página de Busca
  elif pagina_selecionada=="Buscar Jogo":
  st.header("Buscar Informações de Jogo")
  termo_de_busca=st.text_input("Digite o título ou a consulta:")
  if st.button("Buscar"):
  if termo_de_busca:
  with st.spinner("Buscando..."):
  resultados_da_busca=buscar_jogos(termo_de_busca,modelo_gemini)
  if resultados_da_busca:
  st.subheader("Resultados")
  st.markdown(resultados_da_busca,unsafe_allow_html=True)
  else:
  st.info("Nenhum resultado encontrado.")
  else:
  st.warning("Digite um termo de busca.")
 

  #Guia de Cross-Play
  elif pagina_selecionada=="Guia de Cross-Play":
  st.header("Compatibilidade Cross-Play")
  dataframe_crossplay=carregar_dados_crossplay()
  st.dataframe(dataframe_crossplay)
 

  #Página Sobre
  elif pagina_selecionada=="Sobre":
  st.header("Sobre o LagAI")
  st.write("LagAI fornece informações detalhadas sobre jogos online,com foco em cross-play.")
 

 if __name__=="__main__":
  principal()
