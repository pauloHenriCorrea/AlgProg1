""" 
Leia três números com casas decimais (A, B e C) representando os lados de um
triângulo e organize esses lados em ordem decrescente, de tal maneira que A
contenha o maior dos três lados. Logo após, determine o tipo do triângulo que
esses lados formam, baseado nos seguintes casos:

• Se A > B + C, escreva a mensagem: não forma triângulo;
• Se A² = B² + C², escreva a mensagem: triângulo retângulo;
• Se A² > B² + C², escreva a mensagem: triângulo obtusângulo;
• Se A² < B² + C², escreva a mensagem: triângulo acutângulo;
• Se os três lados são iguais, escreva a mensagem: triângulo equilátero;
• Se dois dos três lados são iguais, escreva a mensagem: triângulo isósceles
"""

A = float(input("Informe o valor de A: "))
B = float(input("Informe o valor de B: "))
C = float(input("Informe o valor de C: "))

# * Ordenando A, B e C em ordem decrescente
if A < B:
    A, B = B, A  # ! Essa linha é equivalente ao bloco de cógido abaixo
    # * aux = A
    # * A = B
    # * B = aux
if A < C:
    A, C = C, A  # ! Essa linha é equivalente ao bloco de cógido abaixo
    # * aux = A
    # * A = C
    # * C = aux
if B < C:
    B, C = C, B  # ! Essa linha é equivalente ao bloco de cógido abaixo
    # * aux = B
    # * B = C
    # * C = aux

A_Quadrado = A**2
BCQuadrado = B**2 + C**2
# * Se A > B + C, escreva a mensagem: não forma triângulo

# * Entrada: 9 4 3
if A >= B + C:
    print("Não forma um triângulo")
else:
    # * Se A² = B² + C², escreva a mensagem: triângulo retângulo
    # * Entrada: 5 4 3
    if A_Quadrado == BCQuadrado:
        print("Triângulo retangulo")

    # * Se A² > B² + C², escreva a mensagem: triângulo obtusângulo
    # * Entrada 6 4 3
    elif A_Quadrado > BCQuadrado:
        print("Triângulo obtusângulo")

    # * Se A² < B² + C², escreva a mensagem: triângulo acutângulo
    # * Entrada 6 5 4
    elif A_Quadrado < BCQuadrado:
        print("Triângulo acutângulo")

    # * Se os três lados são iguais, escreva a mensagem: triângulo equilátero
    # * Entrada 2 2 2

    if A == B and B == C:
        print("Triângulo equilátero e ")

    # * Se dois dos três lados são iguais, escreva a mensagem: triângulo isósceles
    # * Entrada 2 8 8
    elif A == B or B == C or A == C:
        print("Triângulo isósceles")


print(A, B, C)
