stop = False

while stop == False:
    coordenadas = input().split()

    x = int(coordenadas[0])
    y = int(coordenadas[1])

    if x != 0 and y != 0:
        if x > 0:
            if y > 0:
                print("primeiro")
            else:
                print("quarto")
        elif x < 0:
            if y > 0:
                print("segundo")
            else:
                print("terceiro")
    else:
        stop = True
