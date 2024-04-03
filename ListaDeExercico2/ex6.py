"""
Escreva um programa que receba dois tempos no formato hh : mm : ss (um
tempo por linha), some os dois tempos e escreva o tempo resultante. Por exemplo, 
para os tempos 03:10:32 e 04:55:40, você deve escrever na tela 08:06:12.
Dica: para ler os tempos, você vai precisar utilizar input.split() de uma forma
diferente da que usamos até agora, procure informações sobre a função split()
do Python.
"""

# Entrada de dados
print("Os tempos inseridos devem ser no formato: hh:mm:ss")
tempo1 = input("Informe o primeiro tempo: ")
tempo2 = input("Informe o segundo tempo: ")

# Computação

# * Convertando os valores inseridos do tipo str para uma lista de strings, str -> list[str]
tempo1Lista = tempo1.split(":")
tempo2Lista = tempo2.split(":")

#! Observação: por padrão, as posições de uma lista ou vetor se iniciam na posição [0]

# * Pegagando somente os valores da primeira posição tanto do tempo1 quanto do tempo 2
posicao1Tempo1 = int(tempo1Lista[0])
posicao1Tempo2 = int(tempo2Lista[0])

# * Pegagando somente os valores da segunda posição tanto do tempo1 quanto do tempo 2
posicao2Tempo1 = int(tempo1Lista[1])
posicao2Tempo2 = int(tempo2Lista[1])

# * Pegagando somente os valores da terceira posição tanto do tempo1 quanto do tempo 2
posicao3Tempo1 = int(tempo1Lista[2])
posicao3Tempo2 = int(tempo2Lista[2])

# * Somando os valores das posições equivalentes
somaDaPosicao1 = int(posicao1Tempo1 + posicao1Tempo2)
somaDaPosicao2 = int(posicao2Tempo1 + posicao2Tempo2)
somaDaPosicao3 = int(posicao3Tempo1 + posicao3Tempo2)

# * Verificando se as horas é maior ou igual a 23
if somaDaPosicao1 > 23:
    # * Pegando somente o resto da divisão da somaDaPosicao1 / 24
    somaDaPosicao1 %= 24

# * Verificando se os minutos é maior que 60
if somaDaPosicao2 > 60:
    # * Adicina a quantidade de minutos que passaram nas horas
    somaDaPosicao1 += int(somaDaPosicao2 / 60)
    # * Pegando somente o resto da divisão da somaDaPosicao2 / 60
    somaDaPosicao2 %= 60

# * Verificando se os segundos é maior que 60
if somaDaPosicao3 > 60:
    # * Adicina a quantidade de minutos que passaram nos segundos
    somaDaPosicao2 += int(somaDaPosicao3 / 60)
    # * Pegando somente o resto da divisão da somaDaPosicao3 / 60
    somaDaPosicao3 %= 60

# * Formatando os dados para imprimir ele na tela
if somaDaPosicao1 == 24:
    somaDaPosicao1 = 0

if somaDaPosicao1 < 10:
    somaDaPosicao1 = "0" + str(somaDaPosicao1)

if somaDaPosicao2 < 10:
    somaDaPosicao2 = "0" + str(somaDaPosicao2)

if somaDaPosicao3 < 10:
    somaDaPosicao3 = "0" + str(somaDaPosicao3)

concatenacao = (
    str(somaDaPosicao1) + ":" + str(somaDaPosicao2) + ":" + str(somaDaPosicao3)
)

# Saída de dados
print(concatenacao)
