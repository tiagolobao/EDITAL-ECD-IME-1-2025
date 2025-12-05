# importando os dados
import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("./B/questao_2.csv")

# Preparando plot de variaveis string
variaveis = ["Estado_civil", "Regiao_de_procedencia"]
for idx, var in enumerate(variaveis):
    plt.subplot(221 + idx)
    dados_processados = dados[var].str.strip()
    plt.bar(dados_processados.unique(), dados_processados.value_counts())

# Preparando plot de variaveis especiais
plt.subplot(223)
dados_processados = dados["N_de_filhos"].astype(int)
plt.bar(dados_processados.unique(), dados_processados.value_counts())

plt.subplot(224)
dados_processados = dados["idade"].astype(int)
plt.bar(dados_processados.unique(), dados_processados.value_counts())

plt.savefig("questao_2.png", dpi=100, bbox_inches="tight", format="png")
