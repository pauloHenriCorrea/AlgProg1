v = input().split()

black_list = []

i = 0

while i < len(v):
    j = 0
    existe = False
    while j < len(black_list):
        if v[i] == black_list[j]:
            existe = True
        j += 1
    if not existe:
        black_list.append(v[i])
    i += 1
print(black_list)
