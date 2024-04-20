pares = 0
impares = 0
positivos = 0
negativos = 0
for n in range(5):
    x = float(input())

    if x % 2 == 0:
        pares += 1
    else:
        impares += 1

    if x > 0:
        positivos += 1
    elif x < 0:
        negativos += 1

print(
    str(pares)
    + " valor(es) par (es)\n"
    + str(impares)
    + " valor(es) impar (es)\n"
    + str(positivos)
    + " valor(es) positivo (s)\n"
    + str(negativos)
    + " valor(es) negativo (s)"
)
