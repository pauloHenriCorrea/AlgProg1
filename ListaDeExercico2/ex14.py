"""
O inverno não é uma estação do ano que agrada a todos, especialmente nos locais onde as temperaturas 
são extremamente baixas. Em alguns locais, o humor das pessoas é definido com base nas tendências 
climáticas. Alguns teóricos acreditam que as temperaturas dos últimos três dias são suficientes para
determinar o humor de qualquer pessoa para o próximo dia. Um importante estudioso do tema conseguiu
decifrar as regras que geram alegria ou tristeza nas pessoas com base nas temperaturas dos últimos 
três dias, sendo elas:

! • Se a temperatura aumentou do primeiro para o segundo dia, mas diminuiu ou permaneceu constante do 
! segundo para o terceiro dia, as pessoas ficam tristes;

! • Se a temperatura aumentou do primeiro para o segundo dia, e também aumentou do segundo para o 
! terceiro dia, mas aumentou do segundo para o terceiro dia menos do que aumentou do primeiro para o 
! segundo dia, as pessoas ficam tristes;

! • Se a temperatura aumentou do primeiro para o segundo dia, e também aumentou do segundo para o 
! terceiro dia, mas aumentou do segundo para o terceiro dia pelo menos do que aumentou do primeiro para
! o segundo dia, as pessoas ficam felizes;

* • Se a temperatura diminuiu do primeiro para o segungo dia, mas aumentou ou permaneceu constante do 
* segundo para o terceiro dia, as pessoas ficam felizes;

* • Se a temperatura diminuiu do primeiro para o segundo dia, e também diminuiu do segundo para o 
* terceiro dia, mas diminuiu do segundo para o terceiro dia menos do que diminuiu do primeiro para o 
* segundo dia, as pessoas ficam felizes;

* • Se a temperatura diminuiu do primeiro para o segundo dia, e também diminuiu do segundo para o 
* terceiro dia, mas diminuiu do segundo para o terceiro dia menos do que diminuiu do primeiro para
* o segundo dia, as pessoas ficam tristes;

todo: • Se a temperatura permaneceu constante do primeiro para o segundo dia, as pessoas ficam felizes se 
todo: a temperatura aumentou do segundo para o terceiro dia, ou tristes caso contrário.

Escreva um programa que recebe três valores (com casas decimais) de temperaturas e escreve se as 
pessoas ficarão tristes ou felizes, de acordo com as regras estabelecidas.
"""

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

elif temp1 == temp2: # Quando a temperatura permanece constante do primeiro para o segundo dia
    if temp3 > temp2:
        print("As pessoas ficam felizes")
    else:
        print("As pessoas ficam tristes")
