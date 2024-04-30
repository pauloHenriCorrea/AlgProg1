"""
Escreva um programa que leia um número e imprima se ele é igual a 5, a 200,
a 400, se está no intervalo entre 500 e 1000, ou se ela está fora dos escopos
anteriores
"""

# Entrada de dados
numero = float(input("Informe um número: "))

# Computação
if numero == 5:
    print("Igual a 5")
elif numero == 200:
    print("Igual a 200")
elif numero == 400:
    print("Igual a 400")
elif numero >= 500 and numero <= 1000:
    print("Está no intervalo entre 500 e 1000")
else:
    print("Está dora dos escopos anteriores")
