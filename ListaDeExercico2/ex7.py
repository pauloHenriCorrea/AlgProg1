"""
Escreva um programa que leia um número e informe se ele é divisível por 10,
por 5 ou por 2 ou se não é divisível por nenhum deles.
"""

# Entrada de dados
numero = float(input("Informe um número: "))

# Computação
if numero % 2 == 0:
    print("Divisível por 2")

if numero % 5 == 0:
    print("Divisível por 5")

if numero % 10 == 0:
    print("Divisível por 10")

if numero % 2 != 0 and numero % 5 != 0 and numero % 10 != 0:
    print("O número informado não é divisivel por nenhuma das opções")
