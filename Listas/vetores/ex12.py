dic = {}

# −1 3 0 5 0 5 −1 2 − 5 0
numeros = input().split()

i = 0

# Coloca 0 de acordo com o tamanho do vetor de números
while i < len(numeros):
    atual = numeros[i]
    dic[atual] = 0
    i += 1
"""
dic[-1] = 0
dic[3] = 0
dic[5] = 0
dic[0] = 0
dic[2] = 0
dic[-5] = 0
"""

i = 0
while i < len(numeros):
    atual = numeros[i]
    dic[atual] += 1
    i += 1

chaves = list(dic.keys())
# list(dic.keys()) retorna o seguinte vetor => ["-1", "3", "5", "0", "2", "-5"]

i = 0

while i < len(chaves):
    chave = chaves[i]
    i += 1
    print(chave + " aconteceu " + str(dic[chave]))
