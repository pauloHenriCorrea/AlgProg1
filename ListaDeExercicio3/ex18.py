N = int(input())

i = 0

apto = 0  # Aprovado
repn = 0  # Reprovado

mediaTurma = 0

while i < N:
    soma = 0
    passo = 0
    media = 0

    # * Pegando as 3 notas de N alunos
    while passo < 3:
        nota = float(input())

        soma += nota
        passo += 1

    media = soma / 3  # * Calculando o média do aluno N
    mediaTurma += media  # * Fazendo

    if media > 5:
        apto += 1
    else:
        repn += 1
    i += 1

    print(mediaTurma / N, apto, repn)
