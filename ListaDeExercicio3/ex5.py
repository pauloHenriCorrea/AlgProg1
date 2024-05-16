print(
    "5) O programa recebe um número inteiro positivo N, e soma a sequência dos N primeiros números inseridos\n"
)
N = int(input())

i = 0

soma = 0

while i < N:
    x = int(input())
    soma += x
    i += 1

print("O resultado dessa soma é: " + str(soma) + "\n")
