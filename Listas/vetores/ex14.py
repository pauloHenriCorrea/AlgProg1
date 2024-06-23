def copia_e_converte(valores, valores_int):
    i = 0
    while i < len(valores):
        valores_int[i] = int(valores[i])
        i += 1
    return valores_int


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


def remrep(lista):
    black_list = []

    i = 0

    while i < len(lista):
        j = 0
        existe = False
        while j < len(black_list):
            if lista[i] == black_list[j]:
                existe = True
            j += 1
        if not existe:
            black_list.append(lista[i])
        i += 1
    return black_list


lista = input().split()
lista_int = [0] * len(lista)
print(ordena(remrep(copia_e_converte(lista, lista_int))))
