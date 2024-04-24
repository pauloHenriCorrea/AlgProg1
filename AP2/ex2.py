"""
Leia 4 números com casas decimais, correspondentes a 4 notas obtidas por um estudante. Calcule a 
média do aluno, assumindo que as notas possuemm peso 2, 3, 4 e 1, respectivamente, e imprima uma 
mensagem contendo a média do aluno. Se a média for maior ou igual a 7 imprima "Aluno aprovado". Se a
média for menor que, imprima a mensagem "Aluno reprovado". Se a média estiver maior que 5 e menor 
que 6.9 (incluindo esses valores), o programa deve imprimir a mensagem "Aluno em exame"

No caso do aluno ficar em exame, leia mais uma nota, que corresponde à nota que o aluno tirou na 
prova de exame. Recalcule a média do aluno somando a nota da prova de exame com a média que ele já 
possuía e divida por 2, e imprima "Aprovado" no caso dessa média ser maior ou igual a 5, e reprovado
caso contrário, juntamente com a média final do aluno.
"""

n1 = float(input("Informe sua priemira nota: "))
n2 = float(input("Informe sua segunda nota: "))
n3 = float(input("Informe sua terceira nota: "))
n4 = float(input("Informe sua quarta nota: "))

n1 *= 2
n2 *= 3
n3 *= 4
n4 *= 1

media = (n1 + n2 + n3 + n4) / 10

if media >= 7:
    print("Aluno aprovado")
elif media >= 5:
    print("Aluno de exame\n")

    exame = float(input("Informe sua nota de exame: "))

    media = (media + exame) / 2

    if media >= 5:
        print("Aprovado")
    else:
        print("Reprovado")

if media < 5:
    print("Aluno reprovado")
print(media)
