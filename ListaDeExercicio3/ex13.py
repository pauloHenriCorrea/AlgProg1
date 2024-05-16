N = int(input())

i = 0
maior = 0
crescente = True

while i < N:
    x = int(input())

    if i == 0:
        maior = x

    if x >= maior:
        maior = x
    else:
        crescente = False
    i += 1

if crescente:
    print("A sequência está em ordem crescente!")
else:
    print("A sequência não está em ordem crescente!")
