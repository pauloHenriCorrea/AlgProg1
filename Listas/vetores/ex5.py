def le_numeros(n):
    numeros = []
    i = 0
    while i < n:
        numero = int(input())

        if numero >= 0 and numero <= 36:
            numeros.append(numero)
            i += 1
        else:
            print("Valor inválido! Informe novamente.")
    return numeros


n = int(input())
valores = le_numeros(n)

# Declarando vetor, e definindo com 37 posicoes
numeros = [0] * 37

""" Exemplo:
  Se i = 2                                                            i -> 0  1 [2]  3  4  5
  Sabendo que valores[i] = valores[2] = 4                       valores -> 2  5 [4]  5  5  5
  E numeros[valores[i]] = numeros[valores[2]] = numeros[4]      numeros -> 0  0  1   0 [2] 4
  Ent, numeros[4] que eh = 0 vai adicionar +1, fazendo a contagem
"""
i = 0
while i < n:
    numeros[valores[i]] += 1
    i += 1
print(numeros)
