gabarito = input().split()

t = len(gabarito)

# Número de alunos que fizeram a prova
n = int(input())

i = 0
while i < n:
    corect = 0
    r_aluno = input().split()
    t_aluno = len(r_aluno)

    # Verifica se foram passadas a 6 possiveis alternativas
    if t_aluno == t:

        c = 0
        while c < t_aluno:
            if r_aluno[c] == gabarito[c]:
                corect += 1
            c += 1
        i += 1
    else:
        print("Por favor, insira as 6 alternativas")
    print(corect)
