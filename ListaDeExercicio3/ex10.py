print(
    "O programa recebe um N (talque N > 0) inteiro, e uma sequência de números inteiros positivos"
)
N = int(input())

i = 0

par = 0
impar = 0

while i < N:
    x = int(input())

    if x % 2 == 0:
        par += 1
    else:
        impar += 1

    i += 1

print(par, impar)
