N = int(input())

l = [0] * 6


def ler_numeros(n):
    i = 0
    l_numeros = []

    while i < n:
        N = int(input())
        if N >= 1 and N <= 6:
            l_numeros.append(N)
            i += 1
        else:
            print("Por favor, insiria um 1 >= n <=6")
    return l_numeros


l_numeros = ler_numeros(N)
print(l_numeros)

i = 0
while i < N:
    l[l_numeros[i] - 1] += 1
    i += 1
print(l)
