dic = {}

# "−1 3 0 5 0 5 −1 2 −5 0"
numeros = input().split(" ")

i = 0
while i < len(numeros):
    atual = numeros[i]
    dic[atual] = 0
    i += 1
# dic['-1'] = 0
# dic['3'] = 0
# dic['0'] = 0
# dic['5'] = 0
# dic['2'] = 0
# dic['-5'] = 0
# dic.keys -> ['-1','3','0','5','2','-5']

# "−1 3 0 5 0 5 −1 2 −5 0"
i = 0
while i < len(numeros):
    # atual = -1, 3
    atual = numeros[i]
    dic[atual] += 1 # dic['-1'] += 1, dic['3'] += 1
    i += 1

chaves = list(dic.keys())
print(chaves)
i = 0
while i < len(chaves):
    chave = chaves[i] # '-1'
    valor = dic[chave] # dic['-1'] = 2 
    print(chave + " aconteceu + " + str(dic[chave]) + " vezes")
    i += 1


