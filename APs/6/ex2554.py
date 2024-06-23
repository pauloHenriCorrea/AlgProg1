N_D = input().split()


def remove_primeiro_elemento(v):
    new_vector = []
    i = 1
    while i < len(v):
        new_vector.append(v[i])
        i += 1
    return new_vector


def vericar_data(datas, comparecer):
    i = 0
    data = ""
    while i < len(datas):
        data = datas[i]

        j = 0
        while j < len(comparecer):
            if comparecer[i][j] != "1":
                return "Pizza antes de FdI"
            i += 1
    return data


n_pessoas = int(N_D[0])
datas_possiveis = int(N_D[1])

i = 0
datas = []
comparecer = []

# Recebe quais são as possíveis datas e quais pessoas podem ir nesta data
while i < datas_possiveis:
    D = input().split()
    datas.append(D[0])
    comparecer.append(remove_primeiro_elemento(D))
    i += 1

print(vericar_data(datas, comparecer))
