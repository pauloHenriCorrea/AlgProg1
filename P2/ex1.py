# Função que pode ser usada futuramente
def troca(x, y):
    aux = x
    x = y
    y = aux
    return x, y


N = int(input())
caracter = input()

A = False
B = False
C = False

# Inserindo o valor da moeda em algum dos copos
if caracter == "A":
    A = True
elif caracter == "B":
    B = True
elif caracter == "C":
    C = True

i = 0

while i < N:
    tm = int(input())  # tipo de movimento = tm
    # Fazendo a troca de posições do copo
    if tm == 1:
        A, B = B, A
    elif tm == 2:
        B, C = C, B
    elif tm == 3:
        A, C = A, C
    i += 1

# Verificando em qual posição está a moeda
if A:
    print("A")
elif B:
    print("B")
elif C:
    print("C")
