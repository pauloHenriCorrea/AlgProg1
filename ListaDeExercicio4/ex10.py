v = input().split()

black_list = []


def existe_no_vetor(v, n):
    existe = False
    j = 0
    while j < len(v):
        if n == v[j]:
            existe = True
        j += 1
    return existe


def numero_de_vezes_repetidos(v, n):
    j = 0
    count = 0
    while j < len(v):
        if n == v[j]:
            count += 1
        j += 1
    return count


i = 0
while i < len(v):
    if numero_de_vezes_repetidos(v, v[i]) > 1 and not existe_no_vetor(black_list, v[i]):
        black_list.append(v[i])
    i += 1
print(black_list)
