"""
Construa um programa para determinar se o indivíduo esta com um peso favorável. 
Essa situação é determinada através do IMC (Índice de Massa Corpórea), 
que é definida como sendo a relação entre o peso (PESO) e o quadrado
da Altura (ALTURA) do indivíduo. Ou seja, IMC = peso/altura² . 
Considere as seguintes informações:
• IMC abaixo de 20: abaixo do peso;
• IMC de 20 até 25: peso normal;
• IMC de 25 até 30: sobrepeso;
• IMC de 30 até 40: obeso;
• IMC acima de 40: obeso mórbido.
"""

# Entrada de dados
height = float(input("Informe sua altura em (m): "))
weight = float(input("Informe seu peso (Kg): "))

# Computação
# * Calculando o IMC
imc = weight / (height * height)

# * Classificando o IMC do usuário
if imc <= 20:
    print("Abaixo do peso")
elif imc <= 25:
    print("Peso normal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("Obeso")
else:
    print("Obeso mórbido")
print(imc)