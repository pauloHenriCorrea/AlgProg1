def dif(v):
    diferenca_um = False

    n = v[0] - v[1]

    i = 2
    while i < len(v) - 1:

        i += 1


def copia_e_converte(v):
    v_int = []

    i = 0
    while i < len(v):
        v_int.append(int(v[i]))
        i += 1
    return v_int


numeros = input().split()

print(copia_e_converte(numeros))
