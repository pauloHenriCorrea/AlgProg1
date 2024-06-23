def exclui_numeros_repetidos(v):
    l = []
    i = 0
    while i < len(v):
        exist = False
        j = 0
        while j < len(l):
            if v[i] == l[j]:
                exist = True
            j += 1
        if not exist:
            l.append(v[i])
        i += 1
    return l


def copia_e_converte(v):
    v_int = []

    i = 0
    while i < len(v):
        v_int.append(int(v[i]))
        i += 1
    return v_int


def intersec(A, B):
    intersecao = []
    i = 0
    while i < len(B):
        j = 0
        while j < len(A):
            if B[i] == A[j]:
                intersecao.append(B[i])
            j += 1
        i += 1
    return intersecao


def ordena(v):
    i = 0
    while i < len(v) - 1:
        j = i + 1
        while j < len(v):
            if v[j] < v[i]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
            j += 1
        i += 1
    return v


A = input().split()
B = input().split()

menor = A
maior = B

if len(A) < len(B):
    menor = B
    maior = A

result = ""
v = ordena(exclui_numeros_repetidos(copia_e_converte(intersec(menor, maior))))

i = 0
while i < len(v):
    if i == len(v) - 1:
        result += str(v[i])
    else:
        result += str(v[i]) + " "
    i += 1
print(result)
