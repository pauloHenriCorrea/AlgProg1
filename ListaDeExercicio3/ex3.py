print(
    "3) O programa recebe um número inteiro positivo N, e imprime o fatorial desse número.\n"
)
print("\nInsira um número inteiro, talque N > 0")

N = int(input())

n = N

fat = 1
vezes = " * "
multi = str(N) + "! = "

while N != 0:
    fat = fat * N

    if N == 1:
        vezes = ""

    multi += str(N) + vezes
    N = N - 1

print("Número informado foi: " + str(n))
print(multi)
print("A multiplicação de " + str(n) + "! é de: " + str(fat) + "\n")
