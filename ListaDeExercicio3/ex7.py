print(
    "O programa recebe um número inteiro positivo N, e fazer a soma dos números pares e dos números ímpares"
)
N = int(input())

i = 0

par = 0
impar = 0

while i < N:
    x = int(input())

    if x % 2 == 0:
        par += x
    else:
        impar += x
    i += 1
print("\nA soma dos números pares é: " + str(par))
print("A soma dos números ímpares é: " + str(impar))
