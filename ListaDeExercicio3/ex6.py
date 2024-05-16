print(
    "O programa recebe um número inteiro positivo N, e calcular qual é a soma dos números positivos que foram inseridos."
)
N = int(input())

i = 0

soma = 0

while i < N:
    x = int(input())
    if x > 0:
        soma += x
    i += 1

print("O resultado dessa soma é: " + str(soma) + "\n")
