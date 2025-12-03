import statistics

def media(v: list[int]) -> float:
    soma = 0
    for e in v:
        soma += e
    return soma / len(v)

def mediana(v: list[int]) -> float:
    ordenado = v
    ordenado.sort()
    tamanho = len(ordenado)

    if tamanho % 2 == 0: # par
        meio = int((tamanho-1) / 2)
        return ( ordenado[meio] + ordenado[meio+1] ) / 2
    else: #impar
        meio = int((tamanho) / 2)
        return ordenado[meio]


lista_1 = [9, 8, 7, 6, 5, 4]
lista_2 = [100, 5, 20, 75, 30]
lista_3 = [15, 27]

print("media\n")

print(" resultado das funcoes implementadas:")
print(f"lista 1: {media(lista_1)}")
print(f"lista 2: {media(lista_2)}")
print(f"lista 3: {media(lista_3)}")
print( "resultado da std lib python:")
print(f"lista 1: {statistics.mean(lista_1)}")
print(f"lista 1: {statistics.mean(lista_2)}")
print(f"lista 1: {statistics.mean(lista_3)}")

print("\nmediana\n")

print(" resultado das funcoes implementadas:")
print(f"lista 1: {mediana(lista_1)}")
print(f"lista 2: {mediana(lista_2)}")
print(f"lista 3: {mediana(lista_3)}")
print( "resultado da std lib python:")
print(f"lista 1: {statistics.median(lista_1)}")
print(f"lista 1: {statistics.median(lista_2)}")
print(f"lista 1: {statistics.median(lista_3)}")
