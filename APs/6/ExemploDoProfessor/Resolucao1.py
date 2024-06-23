def olharctem(lista, n):
    if lista == []:
        return True
    else:
        w = 0
        while w < len(lista):
            if n == lista[w]:
                return False
            w += 1
    return True


sequencia = input().split()
lista = []
x = 0

while x < len(sequencia):
    h = olharctem(lista, int(sequencia[x]))
    count = 1
    if h:
        lista.append(int(sequencia[x]))
        y = x + 1
        while y < len(sequencia):
            if int(sequencia[x]) == int(sequencia[y]):
                count += 1
            y += 1
        print(sequencia[x] + " ocorre " + str(count) + " vez(es)")
    x += 1
