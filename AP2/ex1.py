"""
Receba dois números inteiros e n (entre 1 e 9) e m (entre 1 e 5) e imprima quantos dígitos há no número n**m
"""

n = int(input("Informe um número inteiro entre 1 e 9: "))
m = int(input("Informe um número inteiro entre 1 e 5: "))

calculo = n**m

if calculo < 10:
    print("1 dígito")

elif calculo < 100:
    print("2 dígito")

elif calculo < 1000:
    print("3 dígito")

elif calculo < 10000:
    print("4 dígito")

elif calculo < 100000:
    print("5 dígito")
print(calculo)
