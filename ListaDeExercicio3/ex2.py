print(
    "2) O programa recebe um número inteiro positivo N, e imprime os N primeiros números ímpares.\n"
)
print("\nInsira um número inteiro, talque N > 0")

N = int(input())

i = 1
virgula = ", "
impares = str(i) + virgula

while i <= N * 2:
    if i % 2 != 0 and i != 1:
        impares += str(i) + virgula

    if i == N * 2 - 4:
        virgula = " e "
    if i > N * 2 - 3:
        virgula = ""
    i += 1

print("\nNúmero informado foi: " + str(N))
print("Os " + str(N) + " primeros números impares são: " + impares + "\n")
