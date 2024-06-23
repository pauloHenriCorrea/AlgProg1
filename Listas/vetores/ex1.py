N = int(input())

l = []
l_reverse = []

i = 0
# Recebendo os N números inteiros
while i < N:
    n = int(input())
    l.append(n)
    i += 1

i = len(l) - 1

# Percorrendo o vetor l ao contrário
while i >= 0:
    l_reverse.append(l[i])
    i -= 1
print(l)
print(l_reverse)
