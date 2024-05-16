N = int(input())

i = 0
maior = 0
menor = 100

while i < N:
    x = float(input())

    if x >= 0 and x <= 100:
        if x > maior:
            maior = x
        elif x < menor:
            menor = x
        i += 1
    else:
        print("O número informado está fora do escopo! ")
print(menor, maior)
