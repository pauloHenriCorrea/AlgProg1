"""
Escreva um programa que receba três valores, armazenando-os nas variáveis
x, y e z, e ordene esses valores de modo que, ao final, o menor valor esteja
armazenado na variável x, o valor intermediário esteja armazenado na variável y
e o maior valor esteja armazenado na variável z. Faça a simulação passo a passo
da execução de sua solução.
"""

# Entrada de dados
x = float(input("Insira o primeiro número: "))
y = float(input("Insira o segundo número: "))
z = float(input("Insira o terceiro número: "))

# if x > y and x > z and y < z:
#     # // 3 > 1 < 2
#     # // x > y < z
#     aux = x
#     x = y
#     y = z
#     z = aux
#     print("Primeiro if")
#     print(x, y, z)
# elif x < y and y < z:
#     # // 1 < 2 < 3
#     # // x < y < z
#     x = x
#     y = y
#     z = z
#     print("Segundo if")
#     print(x, y, z)
# elif x > y and y > z and z < y:
#     # // 3 > 2 > 1
#     # // x > y > z
#     aux = x
#     x = z
#     y = y
#     z = aux
#     print("Terceiro IF")
#     print(x, y, z)
# elif x < y and x > z:
#     #  2 < 3 > 1
#     # // x < y > z
#     aux = z
#     z = y
#     y = x
#     x = aux
#     print("Quarto if")
#     print(x, y, z)
# elif x < y and z < y:
#     # // 1 < 3 > 2
#     # // x < y > z
#     aux = y
#     x = x
#     y = z
#     z = aux
#     print("Quinto if")
#     print(x, y, z)
# elif  z > y and z > x:
#     #// 2 > 1 < 3
#     #// x > y < z
#     aux = x
#     x = y
#     y = aux
#     z = z
#     print("Sexto if")
#     print(x, y, z)

if x > y:
    if x > z:
        aux = x
        x = y
        y = z
        z = aux
        print(x, y, z)
    else:
        aux = x
        x = y
        y = aux
        z = z
        print(x, y, z)
elif y > x:
    if y > z:
        aux = y
        x = x
        y = z
        z = aux
        print(x , y, z)
    else:
        x = x
        y = y
        z = z
        print(x , y, z)
        # z eh o maior