def esta_presente(vetor, elemento):
    i = 0
    while i < len(vetor):
        if vetor[i] == elemento:
            return True
        i += 1
    return False

# "−1 3 0 5 0 5 −1 2 − 5 0"
numeros = input() # Todo conjunto de números

# valores[0] = "-1"
# valores[1] = "3"
# valores[2] = "0"
# ...
# valores[9] = "0"
valores = numeros.split(" ")

blacklist = []

i = 0
while i < len(valores):
    alvo = valores[i]
    if esta_presente(blacklist, alvo) == False:
        blacklist.append(alvo)

        # Descobrir quantas vezes "alvo" acontece em numeros
        j = 0
        contador = 0
        while j < len(valores):
            if valores[j] == alvo:
                contador += 1
            j += 1
        
        print(alvo + " aconteceu " + str(contador) + " vez(es)")

    i += 1