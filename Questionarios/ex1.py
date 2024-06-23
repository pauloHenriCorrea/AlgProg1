n = int(input())

i = 0
idade = []
nomes = []

soma = 0
while i < n:
    string = input().split()
    nomes.append(string[0])
    idade.append(int(string[1]))
    soma += int(string[1])
    i += 1

media = soma / n

print("Média: " + str(round(media, 1)))
i = 0
while i < len(idade):
    if idade[i] > media:
        print(nomes[i] + " está acima da média")
    elif idade[i] == media:
        print(nomes[i] + " está igual a média")
    else:
        print(nomes[i] + " está abaixo da média")
    i += 1
