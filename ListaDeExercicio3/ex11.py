i = 1
dia = 0
maior = 0

while i <= 7:
    discosVendidos = float(input())

    if discosVendidos > maior:
        maior = discosVendidos
        dia = i
    i += 1

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
else:
    print("Sábado")
print(maior)
