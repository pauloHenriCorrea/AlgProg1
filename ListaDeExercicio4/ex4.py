N = int(input())
l = [0] * 6

def ler_numeros(n):
    i = 0
    l_numeros = []

    while i < n:
        N = int(input())
        if N >= 0 and N <= 6:
            l_numeros.append(N)
            i += 1
        else:
            print("Por favor, insiria um 0 >= n <=6")