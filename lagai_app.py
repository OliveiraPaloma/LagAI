import streamlit as st
import requests
from bs4 import BeautifulSoup

def buscar_info_techtudo(url="https://www.techtudo.com.br/listas/2024/07/15-jogos-de-ps4-com-crossplay-no-pc-ou-xbox-para-jogar-com-seus-amigos.ghtml"):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para erros HTTP
        soup = BeautifulSoup(response.content, 'html.parser')

        jogos = []
        lista_jogos = soup.find_all('div', class_='list-item') # Inspecionar o site para encontrar o elemento correto

        for item in lista_jogos:
            nome_jogo_element = item.find('a', class_='item-title')
            crossplay_info_element = item.find('div', class_='item-description') # Ajustar conforme a estrutura real

            if nome_jogo_element and crossplay_info_element:
                nome_jogo = nome_jogo_element.text.strip()
                crossplay_info = crossplay_info_element.text.strip()
                jogos.append({"jogo": nome_jogo, "crossplay": crossplay_info, "fonte": "TechTudo"})

        return jogos

    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar o TechTudo: {e}")
        return []

st.title("Resultados de Cross-Play (TechTudo)")
resultados = buscar_info_techtudo()

if resultados:
    for jogo in resultados:
        st.write(f"**Jogo:** {jogo['jogo']}")
        st.write(f"**Cross-Play:** {jogo['crossplay']}")
        st.write(f"**Fonte:** {jogo['fonte']}")
        st.markdown("---")
else:
    st.info("Nenhum resultado encontrado no TechTudo.")
