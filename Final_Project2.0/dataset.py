import pandas as pd

df = pd.read_csv("vendas2.csv", sep=";", decimal=",", encoding="UTF-8")
df["Data Venda"] = pd.to_datetime(df["Data Venda"], dayfirst=True)
df["Vencimento do Titulo"] = pd.to_datetime(df["Vencimento do Titulo"], dayfirst=True)
df = df.sort_values("Data Venda")