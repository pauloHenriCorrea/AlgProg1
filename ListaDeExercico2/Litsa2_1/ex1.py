_id = input("Informe seu número de identificação: ")
p1 = float(input("Informe sua primeira nota: "))
p2 = float(input("Informe sua segunda nota: "))
p3 = float(input("Informe sua terceira nota: "))
ml = float(input("Informe sua média da lista de exercício: "))

conceito = ""

# * Cálculo da média anual do aluno
ma = round((p1 + (p2 * 2) + (p3 * 2) + (ml * 2)) / 7, 2)

# * Verifica qual foi a média anual do aluno
if ma >= 9:
    conceito = "A"
elif ma >= 7.5:
    conceito = "B"
elif ma >= 6:
    conceito = "C"
elif ma >= 4:
    conceito = "D"
else:
    conceito = "E"

# * Verificando se o aluno foi aprovado de acordo com o conceito
if conceito == "A" or conceito == "B" or conceito == "C":
    # * Guarda o valor do conceito para concatenar na linha de baixo
    aux = conceito
    conceito = "aprovado com conceito " + aux
else:
    # * Guarda o valor do conceito para concatenar na linha de baixo
    aux = conceito
    conceito = "reprovado com conceito " + aux

# * Formatando a saída para o usuário
concatenacao = "Sua média anual foi de " + str(ma) + ", e você foi " + conceito

# Saída de dados
print(concatenacao)
