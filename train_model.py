import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

# Crie a pasta "modelos" se não existir
os.makedirs("modelos", exist_ok=True)

# Carrega o dataset CSV com os dados reais
df = pd.read_csv("dados/partidas.csv")

# Exemplo: seleciona features e alvo
# Substitua por suas colunas reais (ajuste conforme necessário)
X = df[["home_goals", "away_goals"]]  # exemplo de colunas
y = df["result"]  # coluna de resultado (Ex: "home_win", "draw", "away_win")

# Divide em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Cria e treina o modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Salva o modelo treinado
with open("modelos/modelo.pkl", "wb") as f:
    pickle.dump(modelo, f)

print("Modelo treinado e salvo com sucesso em modelos/modelo.pkl")
