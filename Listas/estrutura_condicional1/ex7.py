# Entrada de dados
num = float(input("Informe um número: "))

# Computação
if num % 2 == 0:
    print("Divisível por 2")

if num % 5 == 0:
    print("Divisível por 5")

if num % 10 == 0:
    print("Divisível por 10")

if num % 2 != 0 and num % 5 != 0 and num % 10 != 0:
    print("O número informado não é divisivel por nenhuma das opções")
