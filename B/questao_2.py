# importando os dados
import matplotlib.pyplot as plt
import pandas as pd

dados = pd.read_csv("./B/questao_2.csv")
variaveis = ["Estado_civil", "Regiao_de_procedencia", "N_de_filhos", "idade"]


def prepare_plot(dados, variaveis: list[str]):
    for idx, var in enumerate(variaveis):
        plt.subplot(221 + idx)
        if dados[var].dtype == "object":
            counts = dados[var].str.strip().value_counts()
        elif pd.api.types.is_numeric_dtype(dados[var]):
            counts = dados[var].astype(int).value_counts()
        plt.bar(counts.index, counts.values)


prepare_plot(dados, variaveis)

plt.savefig("questao_2_py.png", dpi=100, bbox_inches="tight", format="png")
