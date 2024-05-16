print(
    "\nO programa recebe um número inteiro positivo N, logo após receba a sequência de N números interios, e imprima quantos são positivos e quantps são não-positivos"
)
print("Um número é não-positivo se é negativo ou se é igual a 0 (zero)\n")
N = int(input())
i = 0

positive = 0
notPositive = 0

while i < N:
    x = int(input())

    if x > 0:
        positive += 1
    else:
        notPositive += 1
    i += 1
print("Números negativos: " + str(notPositive))
print("Números positivos: " + str(positive))
