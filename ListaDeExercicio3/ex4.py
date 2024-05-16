print(
    "4) O programa recebe um número inteiro positivo N, e imprima as N primeiras potências de 2\n"
)
print("\nInsira um número inteiro, talque N > 0")

N = int(input())

i = 0

pot = 2**i
concat = ""

while i < N:
    concat += "2^" + str(i) + " = " + str(pot) + " \n"
    pot *= 2
    i += 1
    
print("O número inserido foi: " + str(N))
print(concat)
