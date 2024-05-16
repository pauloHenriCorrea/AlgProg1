print(
    "1) O programa recebe um número inteiro positivo N, soma os N primeiros inteiros positivos, e mostra o resultado na tela.\n"
)
print("\nInsira um número inteiro, talque N > 0")

N = int(input())

result = 0
i = 0
while i <= N:
    result += i
    i += 1
print("\nO número inserido foi: " + str(N))
print("E a soma é: " + str(result) + "\n")
