N = int(input())

i = 0
j = 0

soma = 0

while i < N:
    soma += (i + 1) // (N - j)

    j += 1
    i += 1
print(soma)
