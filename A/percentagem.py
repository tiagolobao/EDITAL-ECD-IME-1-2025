
def calcula_percentagem(numerando: float, dividendo: float) -> float:
    return (numerando / dividendo) * 100

resultado = calcula_percentagem(10,100)
print(f"10 vale {resultado}% de 100 ")

resultado = calcula_percentagem(0.5,50)
print(f"0.5 vale {resultado}% de 50")
