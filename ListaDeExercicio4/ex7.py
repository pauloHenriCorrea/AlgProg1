N = input().split()


def list_nuns(N):

    l = []
    i = 0

    while i < len(N):
        l.append(int(N[i]))
        i += 1
    return l


numeros = list_nuns(N)

menor = numeros[0]

i = 0
while i < len(numeros):
    if numeros[i] < menor:
        menor = numeros[i]
    i += 1
print(menor)
