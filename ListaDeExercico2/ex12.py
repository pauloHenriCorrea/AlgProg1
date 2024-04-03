"""
Faça um programa que recebe a idade e o peso de uma pessoa. De acordo com a
tabela a seguir, verifique e mostre em qual grupo de risco essa pessoa se encaixa.
"""

# Entrada de dados
age = int(input("\nInforme sua idade: "))
weight = float(input("Informe seu peso em Kg: "))

# Computação
# * Esté primeiro if verifica se a idade da pessoa é menor que 20
if age < 20:
    print("\nIdade menor que 20")

    if weight <= 60:
        (print("Peso menor ou igual a 60"))
    elif weight <= 90:
        print("Peso maior que 60 ou menor ou igual a 90")
    else:
        print("Peso acima de 90")

    # * Esté segundo if verifica se a idade da pessoa é maior ou igual a 20 e menor ou igual a 50
elif age <= 50:
    print("\nIdade maior ou igual a 20 e menor ou igual a 50")

    if weight <= 60:
        print("Peso menor ou igual a 60")
    elif weight <= 90:
        print("Peso maior que 60 ou menor ou igual a 90")
    else:
        print("Peso acima de 90")

    # * Caso a idade da pessoa for acima de 50, será executado o bloco de intruções abaixo
else:
    print("\nSua idade é acima de 50")

    if weight <= 60:
        print("Peso menor ou igual a 60")
    elif weight <= 90:
        print("Peso maior que 60 ou menor ou igual a 90")
    else:
        print("Peso acima de 90")
