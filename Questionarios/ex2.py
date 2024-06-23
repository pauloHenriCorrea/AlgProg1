n = int(input())

numeros = input().split()


def copia_e_converte(v):
    v_int = []

    i = 0
    while i < len(v):
        v_int.append(int(v[i]))
        i += 1
    return v_int


def acha_menor_valor(v):
    menor = v[0]

    l = [0] * 2

    i = 0
    while i < len(v):
        if v[i] < menor:
            menor = v[i]
            l[0] = menor
            l[1] = i

        i += 1
    return l


v = acha_menor_valor(copia_e_converte(numeros))
print("Menor valor: " + str(v[0]))
print("Posicao: " + str(v[1]))
