def copia_e_converte(v):
    v_int = []

    i = 0
    while i < len(v):
        v_int.append(int(v[i]))
        i += 1
    return v_int


def dif(v, i):
    diferenca = v[i] - v[i + 1]
    # Pega o módulo da diferença
    if diferenca < 0:
        diferenca *= -1
    return diferenca


def uns(contadores):
    diferencas = []
    i = 0
    while i < len(contadores):
        if i != len(contadores) - 1:
            diferenca = dif(contadores, i)
            diferencas.append(diferenca)
        i += 1
    i = 0
    return diferencas


def sequncia_cheia(vetor):
    numeros = []
    i = 1
    while i <= len(vetor):
        numeros.append(i)
        i += 1

    l = []
    v = False

    i = 1
    while i <= len(vetor):
        j = 0
        while j < len(vetor):
            if numeros[i - 1] == vetor[j]:
                v = True
            j += 1
        i += 1
        l.append(v)
    i = 0

    while i < len(l):
        if not l[i]:
            return False
        i += 1

    return True


numeros = input().split()

print(sequncia_cheia(uns(copia_e_converte(numeros))))
