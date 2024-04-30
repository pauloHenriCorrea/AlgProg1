def main():
    print("___________________________________________________")
    print("\n\n Informe abaixo, qual exercício você deseja fazer\n")
    print("___________________________________________________\n")

    parans = int(input())

    print("Neste exercício você deve:")
    match parans:
        case 1:
            um()

        case 2:
            dois()

        case 3:
            tres()

        case 4:
            quatro()

        case 5:
            cinco()

        case 6:
            seis()

        case 7:
            sete()

        case 8:
            oito()

        case 9:
            nove()

        case 10:
            dez()

        case 11:
            onze()

        case 12:
            doze()

        case 13:
            treze()

        case 14:
            quatorze()

        case 15:
            quinze()

        case 16:
            dezesseis()

        case 17:
            dezessete()

        case 18:
            dezoito()

        case 19:
            dezenove()

        case 20:
            vinte()

        case 21:
            vinte_e_um()

        case 22:
            vinte_e_dois()

        case 23:
            vinte_e_tres()


####################################################################################################
def um():
    print("-> Escrever um programa que recebe um número inteiro positivo N")
    print("-> Somar os N primeiros inteiros positivos e mostra o resultado na tela")
    N = int(input())

    i = 1

    soma = 0

    while i <= N:
        soma += i
        i += 1
    print(soma)


####################################################################################################
def dois():
    print("-> Escrever um programa que recebe um número inteiro positivo N")
    print("-> Imprimir os N primeiros números ímpares naturais")
    N = int(input())

    i = 1

    impares = 1

    while i <= N * 2:
        if i % 2 != 0:
            print(impares)
            impares += 2
        i += 1


####################################################################################################
def tres():
    N = int(input())

    fat = 1

    while N != 0:
        fat = fat * (N)
        N = N - 1
    print(fat)


####################################################################################################
def quatro():
    N = int(input())

    i = 0

    pot = 2**i

    while i < N:
        print(pot)
        pot *= 2
        i += 1


####################################################################################################
def cinco():
    N = int(input())

    i = 0

    soma = 0

    while i < N:
        x = int(input())
        soma += x
        i += 1
    print(soma)


####################################################################################################
def seis():
    N = int(input())

    i = 0

    soma = 0

    while i < N:
        x = int(input())

        if x > 0:
            soma += x
        i += 1

    print(soma)


####################################################################################################
def sete():
    N = int(input())

    i = 0

    par = 0
    impar = 0

    while i < N:
        x = int(input())

        if x % 2 == 0:
            par += x
        else:
            impar += x
        i += 1

    print(par, impar)


####################################################################################################
def oito():
    i = 0

    abaixo = 0

    while i < 7:
        celsius = float(input())

        if celsius < 0:
            abaixo += 1
        i += 1

    print(abaixo)


####################################################################################################
def nove():

    N = int(input())

    i = 0

    positive = 0
    notPositive = 0

    while i < N:
        x = int(input())

        if x > 0:
            positive += 1
        else:
            notPositive += 1

        i += 1

    print(positive, notPositive)


####################################################################################################
def dez():
    N = int(input())

    i = 0

    par = 0
    impar = 0

    while i < N:
        x = int(input())

        if x % 2 == 0:
            par += 1
        else:
            impar += 1

        i += 1

    print(par, impar)


####################################################################################################
def onze():
    i = 1
    dia = 0
    maior = 0

    while i <= 7:
        discosVendidos = float(input())

        if i == 1:
            maior = discosVendidos

        if discosVendidos > maior:
            maior = discosVendidos
            dia = i
        i += 1

    if i == 1:
        print("Domingo")
    elif i == 2:
        print("Segunda")
    elif i == 3:
        print("Terça")
    elif i == 4:
        print("Quarta")
    elif i == 5:
        print("Quinta")
    elif i == 6:
        print("Sexta")
    else:
        print("Sábado")
    print(maior)


####################################################################################################
def doze():
    N = int(input())

    i = 0
    maior = 0
    menor = 100

    while i < N:
        x = float(input())

        if x >= 0 and x <= 100:
            if x > maior:
                maior = x
            elif x < menor:
                menor = x
            i += 1
        else:
            print("O número informado está fora do escopo! ")
    print(menor, maior)


####################################################################################################
def treze():
    N = int(input())

    i = 0
    maior = 0
    crescente = True

    while i < N:
        x = int(input())

        if i == 0:
            maior = x

        if x >= maior:
            maior = x
        else:
            crescente = False
        i += 1

    if crescente:
        print("A sequência está em ordem crescente!")
    else:
        print("A sequência não está em ordem crescente!")


####################################################################################################
def quatorze():
    N = int(input())

    i = 0

    iguais = ""
    ultimoDigito = N % 10
    N = N // 10

    while N > 0:
        proximoDigito = N % 10

        if ultimoDigito == proximoDigito:
            if i % 2 == 0:
                iguais += str(ultimoDigito) + str(proximoDigito)
            else:
                iguais += str(ultimoDigito)
            print(iguais)
        else:
            i = 0
        ultimoDigito = proximoDigito
        N = N // 10
        i += 1


####################################################################################################
def quinze():
    N = int(input())

    i = 0

    ultimoDigito = N % 10
    N //= 10

    while N > 0:
        proximoDigito = N % 10
        if N < 10:
            if proximoDigito == ultimoDigito:
                print("São iguais")
            else:
                print("Não são iguais")
        N = N // 10


####################################################################################################
def dezesseis():
    N = int(input())
    i = int(input())
    j = int(input())

    contador = 0  # Está variável serva para armazenar a quantidade de números que são multiplo de i ou j
    passo = 0
    while contador < N:
        if passo % i == 0 or passo % j == 0:
            print(passo)
            contador += 1
        passo += 1


####################################################################################################
def dezessete():
    N = int(input())

    i = 0
    par = 0
    impar = 0

    while i < N:
        passo = True
        while passo != False:
            x = int(input())
            if x == 0:
                passo = False
            if x % 2 == 0:
                par += x
            else:
                impar += x
        i += 1
        print(par, impar)


####################################################################################################
def dezoito():
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


####################################################################################################
def dezenove():
    N = int(input())

    i = 0
    j = 0

    soma = 0

    while i < N:
        soma += (i + 1) // (N - j)

        j += 1
        i += 1
    print(soma)


####################################################################################################
def vinte():
    def mdc():
        a = int(input())
        b = int(input())

        i = 0

        menorDiv = 1
        maiorDiv = 0

        if a < b:
            i += a
        else:
            i += b

        while i > menorDiv:
            if a % i == 0 and b % i == 0:
                maiorDiv += i
                if maiorDiv != 0:
                    i = 0
            i -= 1
        print(maiorDiv)
    mdc()


####################################################################################################
def vinte_e_um():
    print()


####################################################################################################
def vinte_e_dois():
    print()


####################################################################################################
def vinte_e_tres():
    print()


main()
