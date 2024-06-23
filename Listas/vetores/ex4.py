# Entrada de dados
N = int(input())

l = [0] * 6


# Essa função lê os n números desejados pelo usuário. O parâmetro "n" é o numero n digitado pelo usuário
def ler_numeros(n):
    # Inicializando as váriaveis
    i = 0
    l_numeros = []  # vetor de números

    while i < n:
        N = int(input())
        if N >= 1 and N <= 6:
            l_numeros.append(N)
            i += 1
        else:
            print("Por favor, insiria um 1 >= n <=6")
    return l_numeros


l_numeros = ler_numeros(N)

i = 0
while i < N:
    # Adicina a quantidade de vezes que o número do dado saiu
    l[l_numeros[i] - 1] += 1
    i += 1

# Saída de dados
print(l)
