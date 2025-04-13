from flask import Flask
from predictor import prever_partidas_hoje
from telegram import enviar_mensagem_telegram

app = Flask(__name__)

@app.route('/')
def bot():
    mensagens = prever_partidas_hoje()
    if not mensagens:
        return "Nenhuma previsão feita hoje."
    
    for msg in mensagens:
        enviar_mensagem_telegram(msg)
    
    return "Previsões enviadas com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
