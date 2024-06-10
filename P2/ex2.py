n = int(input())

# A
def fib(n):
    anterior = 1
    atual = 1
    i = 2

    while i < n:
        valor = atual
        atual = anterior + atual
        anterior = valor
        i += 1
    return atual

# B
def fibonorial(n):
    produto = 1
    i = 2

    while i <= n:
        produto *= fib(i)
        i += 1
    return produto

# C
N = int(input())
# 1 1 2 3 5 8