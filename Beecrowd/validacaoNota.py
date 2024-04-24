soma = 0
i = 1

while i != 3:  # Condição de continuação
    nota = float(input())

    if nota >= 0 and nota <= 10:
        soma += nota
        i += 1

        # Condição de parada
        if i == 3:
            media = soma / 2
            print("media = " + str(media))
    else:
        print("nota invalida")
