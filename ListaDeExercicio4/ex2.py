# Quantidade de dias da semana
N = int(input())

i = 0

temperaturas = []
soma = 0

while i < N:
    # Temperatura dos respctivos dias
    n = int(input())
    soma += n
    temperaturas.append(n)
    i += 1
m = soma / N

c = 0
i = 0

while i < len(temperaturas):
    if temperaturas[i] > m:
        c += 1
    i += 1
print(m)
print(c)
