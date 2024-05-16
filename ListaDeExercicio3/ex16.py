N = int(input())
i = int(input())
j = int(input())

contador = 0  # Está variável serva para armazenar a quantidade de números que são multiplo de i ou j
passo = 0
while contador < N:
    if passo % i == 0 or passo % j == 0:
        print(passo)
        contador += 1
    passo += 1
