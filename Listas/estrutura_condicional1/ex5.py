# Entrada de dados
x = float(input("Insira o primeiro número: "))
y = float(input("Insira o segundo número: "))
z = float(input("Insira o terceiro número: "))

"""
if x > y and x > z and y < z:
    # // 3 > 1 < 2
    # // x > y < z
    aux = x
    x = y
    y = z
    z = aux
    print("Primeiro if")
    print(x, y, z)
elif x < y and y < z:
    # // 1 < 2 < 3
    # // x < y < z
    x = x
    y = y
    z = z
    print("Segundo if")
    print(x, y, z)
elif x > y and y > z and z < y:
    # // 3 > 2 > 1
    # // x > y > z
    aux = x
    x = z
    y = y
    z = aux
    print("Terceiro IF")
    print(x, y, z)
elif x < y and x > z:
    #  2 < 3 > 1
    # // x < y > z
    aux = z
    z = y
    y = x
    x = aux
    print("Quarto if")
    print(x, y, z)
elif x < y and z < y:
    # // 1 < 3 > 2
    # // x < y > z
    aux = y
    x = x
    y = z
    z = aux
    print("Quinto if")
    print(x, y, z)
elif z > y and z > x:
    # // 2 > 1 < 3
    # // x > y < z
    aux = x
    x = y
    y = aux
    z = z
    print("Sexto if")
    print(x, y, z)


* Esse bloco de código equivale ao que está em cima, ambos ordena em ordem crescente e coloca o menor valor em x, o intermediário em y e o maior em z
* a diferença a quantidade é quantidade de processamento que o computador tem que fazer, para ordenar os números.
"""

# Computação
# * Verifica se x > y, se for eles fazem a troca, caso contrário x e y já estão ordenados
if x > y:
    # Isso aqui é a mesma coisa que está em baixo, só que de uma forma simplificada
    x, y = y, x
    # aux = x
    # x = y
    # y = aux

# * Verifica se x > z, se for eles fazem a troca, caso contrário x e z já estão ordenados
if x > z:
    x, z = z, y
    # aux = x
    # x = z
    # z = aux

# * Verifica se x > z, se for eles fazem a troca, caso contrário x e z já estão ordenados
if y > z:
    y, z = z, y
    # aux = y
    # y = z
    # z = aux

# Saída
print(x, y, z)
