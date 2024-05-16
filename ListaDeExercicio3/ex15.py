N = int(input())

i = 0

ultimoDigito = N % 10
N //= 10

while N > 0:
    proximoDigito = N % 10
    if N < 10:
        if proximoDigito == ultimoDigito:
            print("São iguais")
        else:
            print("Não são iguais")
    N = N // 10
