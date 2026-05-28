
import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Mês": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "Vendas": [1200, 1500, 1800, 1700, 2100, 2500],
    "Clientes": [50, 65, 80, 74, 95, 110]
}

df = pd.DataFrame(dados)

print(df.describe())

plt.figure(figsize=(7,4))
plt.plot(df["Mês"], df["Vendas"], marker="o")
plt.title("Evolução das Vendas")

plt.savefig("grafico.png")
plt.close()
