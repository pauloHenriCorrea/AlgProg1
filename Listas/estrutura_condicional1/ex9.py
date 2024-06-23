# Entrada de dados
height = float(input("Informe sua altura em (m): "))
weight = float(input("Informe seu peso (Kg): "))

# Computação
# * Calculando o IMC
imc = weight / (height * height)

# * Classificando o IMC do usuário e retorna para o usuário
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
