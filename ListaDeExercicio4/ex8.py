N = input().split()


def list_nuns(N):
    l = []
    i = 0

    while i < len(N):
        l.append(int(N[i]))
        i += 1
    return l


"""
 |  |
[5, 2, 4, 3, 1] menor, troca => [2, 5, 4, 3, 1]

comparando o valor de numeros[0] com os demais valores, para se existe um menor que ele
 |  |
[2, 5, 4, 3, 1] não é menor
 |     |
[2, 5, 4, 3, 1] não é menor
 |        |
[2, 5, 4, 3, 1] não é menor
 |           |
[2, 5, 4, 3, 1] menor, troca => 
"""

numeros = list_nuns(N)
i = 0
while i < len(numeros) - 1:
    j = i + 1
    while j < len(numeros):
        if numeros[j] < numeros[i]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux
        j += 1
    i += 1
print(numeros)
