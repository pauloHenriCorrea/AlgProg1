# Entrada de dados
print("Os tempos inseridos devem ser no formato: hh:mm:ss")
time1 = input("Informe o primeiro tempo: ")
time2 = input("Informe o segundo tempo: ")


# Computação
def mySplit(strings, separator):
    l = []
    cursor = ""

    for char in strings:
        if char == separator:
            l.append(cursor)
            cursor = ""
            continue
        cursor += char

    l.append(cursor)
    return l


# * Convertando os valores inseridos do tipo str para uma lista de strings, str -> list[str]
timeList1 = mySplit(time1, ":")
timeList2 = mySplit(time2, ":")

#! Observação: por padrão, as posições de uma lista ou vetor se iniciam na posição [0]

# * Pegagando somente os valores da primeira posição tanto do tempo1 quanto do tempo 2
position1time1 = int(timeList1[0])
position1time2 = int(timeList2[0])

# * Pegagando somente os valores da segunda posição tanto do tempo1 quanto do tempo 2
position2time1 = int(timeList1[1])
position2time2 = int(timeList2[1])

# * Pegagando somente os valores da terceira posição tanto do tempo1 quanto do tempo 2
position3time1 = int(timeList1[2])
position3time2 = int(timeList2[2])

# * Somando os valores das posições equivalentes
sumPosition1 = int(position1time1 + position1time2)
sumPosition2 = int(position2time1 + position2time2)
sumPosition3 = int(position3time1 + position3time2)

# * Verificando se as horas é maior ou igual a 23
if sumPosition1 > 23:
    # * Pegando somente o resto da divisão da somaDaPosicao1 / 24
    sumPosition1 %= 24

# * Verificando se os minutos é maior que 60
if sumPosition2 > 60:
    # * Adicina a quantidade de minutos que passaram nas horas
    sumPosition1 += int(sumPosition2 / 60)
    # * Pegando somente o resto da divisão da somaDaPosicao2 / 60
    sumPosition2 %= 60

# * Verificando se os segundos é maior que 60
if sumPosition3 > 60:
    # * Adicina a quantidade de minutos que passaram nos segundos
    sumPosition2 += int(sumPosition3 / 60)
    # * Pegando somente o resto da divisão da somaDaPosicao3 / 60
    sumPosition3 %= 60

# * Formatando os dados para imprimir ele na tela
if sumPosition1 == 24:
    sumPosition1 = 0

if sumPosition1 < 10:
    sumPosition1 = "0" + str(sumPosition1)

if sumPosition2 < 10:
    sumPosition2 = "0" + str(sumPosition2)

if sumPosition3 < 10:
    sumPosition3 = "0" + str(sumPosition3)

concat = str(sumPosition1) + ":" + str(sumPosition2) + ":" + str(sumPosition3)

# Saída de dados
print(concat)
