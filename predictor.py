import requests
import pickle
import pytz
from datetime import datetime
import os

def carregar_modelo():
    with open('modelos/modelo.pkl', 'rb') as f:
        return pickle.load(f)

def buscar_jogos_hoje():
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {
        "x-apisports-key": os.getenv("API_FOOTBALL_KEY")
    }
    hoje = datetime.utcnow().strftime('%Y-%m-%d')
    params = {"date": hoje, "timezone": "UTC"}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return []

    data = response.json().get("response", [])
    return data

def prever_partidas_hoje():
    modelo = carregar_modelo()
    partidas = buscar_jogos_hoje()
    mensagens = []

    for jogo in partidas:
        home = jogo["teams"]["home"]["name"]
        away = jogo["teams"]["away"]["name"]
        liga = jogo["league"]["name"]
        horario_utc = jogo["fixture"]["date"]

        try:
            horario_br = datetime.fromisoformat(horario_utc[:-1]).astimezone(
                pytz.timezone("America/Sao_Paulo")
            ).strftime('%d/%m/%Y %H:%M')
        except Exception:
            horario_br = "Horário indefinido"

        # Exemplo de entrada fictícia (ajuste conforme seus dados reais)
        entrada = [[1, 2]]
        resultado = modelo.predict(entrada)[0]
        probas = modelo.predict_proba(entrada)[0]
        confianca = round(max(probas) * 100, 2)

        mensagens.append(
            f"**{home} vs {away}**\n"
            f"Liga: {liga}\n"
            f"Data/Hora: {horario_br}\n"
            f"Previsão: {resultado}\n"
            f"Confiança: {confianca}%"
        )

    return mensagens
