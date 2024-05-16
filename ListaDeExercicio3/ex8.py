print("Insira a quais foram as temperas médias nesta semana")
i = 1

abaixo = 0

while i <= 7:
    celsius = float(input("Dia " + str(i) + ": "))

    if celsius < 0:
        abaixo += 1
    i += 1

if abaixo == 0:
    print("Nenhum dia da semana a temperatura foi abaixo de 0")
elif abaixo == 1:
    print("Durante está semana teve 1 dia que a temperatura foi abaixo de 0")
else:
    print(
        "Durante a semana teve "
        + str(abaixo)
        + " dias da semana que a temperatura foi a abaixo de 0"
    )
print("\n")
