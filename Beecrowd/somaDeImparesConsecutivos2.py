N = int(input())
l = []
for i in range(N):
    x = input().split()

    x0 = int(x[0])
    x1 = int(x[1])
    soma = 0

    # * Trocando x0 com x1, caso x0 > x1
    if x0 > x1:
        aux = x0
        x0 = x1
        x1 = aux

    # * Este for executa no intervalo dos números informados, por exemplo, de 3 a 10
    for X in range(x0 + 1, x1, 1):
        # * Fazendo a soma, somente quando os valores são impares
        if X % 2 != 0:
            soma += X
    l.append(soma)

for x in l:
    print(x)
