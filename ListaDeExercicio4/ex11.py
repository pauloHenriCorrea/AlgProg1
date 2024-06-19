# 2 12 3 6 16 15
numeros = input()

valores = numeros.split()
valores_int = [0] * len(valores)


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


l = copia_e_converte(valores, valores_int)
l_ordenada = ordena(l)

t = len(l_ordenada) - 1
soma = l_ordenada[0] + l_ordenada[t]
i = 0
balanceada = True
while i < len(l_ordenada):
    s = 0
    s = l_ordenada[i] + l_ordenada[t - i]

    if s != soma:
        balanceada = False
    i += 1
print(l_ordenada)
print(balanceada)
