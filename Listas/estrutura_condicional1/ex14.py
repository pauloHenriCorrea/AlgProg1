# Entrada de dados
temp1 = float(input("Informe a temperatura no primeiro dia: "))
temp2 = float(input("Informe a temperatura no segundo dia: "))
temp3 = float(input("Informe a temperatura no terceiro dia: "))

difTemp1Temp2 = temp2 - temp1
difTemp2Temp3 = temp3 - temp2

if temp2 < temp1:  # Quando a temperatura diminuiu do primeiro para o segundo dia
    if temp3 >= temp2:
        print("As pessoas ficam felizes")
    elif temp3 < temp2 and (temp3 - temp2) < (temp2 - temp1):
        print("As pessoas ficam felizes")
    elif temp3 < temp2 and (temp3 - temp2) >= (temp2 - temp1):
        print("As pessoas ficam tristes")

elif temp2 > temp1:  # Quando a temperatura aumentou do primeiro para o segundo dia
    if temp3 <= temp2:
        print("As pessoas ficam tristes")
    elif temp3 > temp2 and (temp3 - temp2) < (temp2 - temp1):
        print("As pessoas ficam tristes")
    elif temp3 < temp2 and (temp3 - temp2) >= (temp2 - temp1):
        print("As pessoas ficam felizes")

elif (
    temp1 == temp2
):  # Quando a temperatura permanece constante do primeiro para o segundo dia
    if temp3 > temp2:
        print("As pessoas ficam felizes")
    else:
        print("As pessoas ficam tristes")
