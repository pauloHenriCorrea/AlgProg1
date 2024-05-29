import os


####################################################################################################
def clear():
    os.system("cls")


####################################################################################################
def one():
    print(
        "1) O programa recebe um número inteiro positivo N, soma os N primeiros inteiros positivos, e mostra o resultado na tela.\n"
    )
    print("\nInsira um número inteiro, talque N > 0")

    N = int(input())
    clear()
    i = 1

    mais = " + "

    if N == 1:
        mais = ""

    soma = str(i) + mais
    result = 0

    while i <= N:
        if i == N:
            mais = ""

        if i > 1 and i <= N:
            soma += str(i) + mais

        result += i
        i += 1
    print("O número inserido foi: " + str(N))
    print("A soma desse número é: " + soma)
    print("E o resultado da soma é: " + str(result) + "\n")


####################################################################################################
def two():
    print(
        "2) O programa recebe um número inteiro positivo N, e imprime os N primeiros números ímpares.\n"
    )
    print("\nInsira um número inteiro, talque N > 0")

    N = int(input())
    clear()

    i = 1
    virgula = ", "
    impares = str(i)

    while i <= N * 2:

        if i == N * 2 - 1:
            virgula = " e "
        elif i == N * 2:
            virgula = ""
        else:
            virgula = ", "
        if i % 2 != 0 and i != 1:
            impares += virgula + str(i)
        i += 1

    print("Número informado foi: " + str(N))
    print("Os " + str(N) + " primeros números impares são: " + impares + "\n")


####################################################################################################
def three():
    print(
        "3) O programa recebe um número inteiro positivo N, e imprime o fatorial desse número.\n"
    )
    print("\nInsira um número inteiro, talque N > 0")

    N = int(input())
    clear()

    n = N

    fat = 1
    vezes = " * "
    multi = str(N) + "! = "

    while N != 0:
        fat = fat * N

        if N == 1:
            vezes = ""

        multi += str(N) + vezes
        N = N - 1

    print("Número informado foi: " + str(n))
    print(multi)
    print("A multiplicação de " + str(n) + "! é de: " + str(fat) + "\n")


####################################################################################################
def four():
    print(
        "4) O programa recebe um número inteiro positivo N, e imprima as N primeiras potências de 2\n"
    )
    print("\nInsira um número inteiro, talque N > 0")

    N = int(input())
    clear()

    i = 0

    pot = 2**i
    concat = ""

    while i < N:
        concat += "2^" + str(i) + " = " + str(pot) + " \n"
        pot *= 2
        i += 1
    print("O número inserido foi: " + str(N))
    print(concat)


####################################################################################################
def five():
    print(
        "5) O programa recebe um número inteiro positivo N, e soma a sequência dos N primeiros números inseridos\n"
    )
    N = int(input())
    clear()

    i = 0

    soma = 0
    conct = ""
    sinal = " + "
    while i < N:
        x = int(input())

        if x < 0:
            sinal = " - "
            y = x * (-1)
        else:
            sinal = " + "

        if i == 0:
            conct += str(x)
        else:
            if x > 0:
                conct += sinal + str(x)
            else:
                conct += sinal + str(y)
        soma += x
        i += 1

    if N == 0:
        print("\n Por favor, insira um número maior que 0\n ")
        five()
    elif N == 1:
        print("Você inseriu 1 número")
        print("A soma é: 1")
    else:
        print("Você inseriu " + str(N) + " números")
        print("A soma desses números é: " + conct)
    print("O resultado dessa soma é: " + str(soma) + "\n")


####################################################################################################
def six():
    print(
        "O programa recebe um número inteiro positivo N, e cálcula qual é a soma dos N números positivos que foram inseridos."
    )
    N = int(input())

    i = 0

    soma = 0

    sinal = " + "
    concat = ""
    while i < N:
        x = int(input())

        if i == N - 1:
            sinal = ""
        if x > 0:
            soma += x
            concat += str(x) + sinal
        i += 1

    clear()
    print("A soma é: " + concat)
    print("O resultado dessa soma é: " + str(soma) + "\n")


####################################################################################################
def seven():
    print(
        "O programa recebe um número inteiro positivo N, e fazer a soma dos números pares e dos números ímpares"
    )
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


####################################################################################################
def eight():
    print("Insira a quais foram as temperas médias nesta semana")
    i = 1

    abaixo = 0

    while i <= 7:
        celsius = float(input("Dia " + str(i) + ": "))

        if celsius < 0:
            abaixo += 1
        i += 1

    clear()

    if abaixo == 0:
        print("Nenhum dia da semana a temperatura foi abaixo de 0")
    elif abaixo == 1:
        print("Durante está semana teve 1 dia que a temperatura foi abaixo de 0")
    else:
        print(
            "Durante a semana teve "
            + str(abaixo)
            + " dias da semana que a temperatura foi a abaixo de 0"
        )
    print("\n")


####################################################################################################
def nine():
    print(
        "\nO programa recebe um número inteiro positivo N, logo após receba a sequência de N números interios, e imprima quantos são positivos e quantps são não-positivos"
    )
    print("Um número é não-positivo se é negativo ou se é igual a 0 (zero)\n")
    N = int(input())
    clear()

    i = 0

    virgula = ""

    positive = 0
    concatPositive = ""

    concatNegatitive = ""
    notPositive = 0

    while i < N:
        x = int(input())

        if positive == 0 or notPositive == 0:
            virgula = ""

        if x > 0:
            if positive > 0:
                virgula = ", "
            concatPositive += virgula + str(x)
            positive += 1
        else:
            if notPositive > 0:
                virgula = ", "
            concatNegatitive += virgula + str(x)
            notPositive += 1
        i += 1

    clear()
    print("\n")
    if N == 1 and N != 0:
        print("Você desejava inserir " + str(N) + " número")
    else:
        print("Você desejava inserir " + str(N) + " números")

    if notPositive == 1 and notPositive != 0:
        print("Você inseriu um número negativos e ele é: " + concatNegatitive)
    else:
        print(
            "Você inseriu "
            + str(notPositive)
            + " números negativos e eles são: "
            + concatNegatitive
        )

    if positive == 1 and positive != 0:
        print("Você inseriu um número positivo e ele é: " + concatPositive)
    else:
        print(
            "Você inseriu "
            + str(positive)
            + " números positivos e eles são: "
            + concatPositive
        )
    print("\n")


####################################################################################################
def ten():
    print(
        "O programa recebe um N (talque N > 0) inteiro, e uma sequência de números inteiros positivos"
    )
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
def eleven():
    i = 1
    dia = 0
    maior = 0

    while i <= 7:
        discosVendidos = float(input())

        if discosVendidos > maior:
            maior = discosVendidos
            dia = i
        i += 1

    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda")
    elif dia == 3:
        print("Terça")
    elif dia == 4:
        print("Quarta")
    elif dia == 5:
        print("Quinta")
    elif dia == 6:
        print("Sexta")
    else:
        print("Sábado")
    print(maior)


####################################################################################################
def twelven():
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
def thirteen():
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
def fourteen():
    N = int(input())

    iguais = ""
    encontrei = False
    ultimoDigito = N % 10

    N = N // 10

    while N > 0 and encontrei == False:
        proximoDigito = N % 10

        if ultimoDigito == proximoDigito:
            iguais += str(ultimoDigito) + str(proximoDigito)
            encontrei = True
        ultimoDigito = proximoDigito
        N = N // 10

    clear()
    print("O número informado foi: " + str(N))
    if encontrei:
        print("Sim")
    else:
        print("Não")


####################################################################################################
def fifteen():
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
def sixteen():
    N = int(input())
    i = int(input())
    j = int(input())

    # clear()

    contador = 0  # Está variável serva para armazenar a quantidade de números que são multiplo de i ou j
    passo = 0

    while contador < N:
        if passo % i == 0 or passo % j == 0:
            print(passo)
            contador += 1
        passo += 1


####################################################################################################
def seventeen():
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
def eighteen():
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
def nineteen():
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
def twenty():
    print("Informe se você deseja fazer o exercício A ou B:")
    chose_user = input()

    def A(N1, N2):
        mdc = 1
        i = 0

        if N1 < N2:
            i = N1
        else:
            i = N2

        while i > 1:
            if N1 % i == 0 and N2 % i == 0:
                mdc = i
                if mdc != 0:
                    i = 0
            i -= 1
        return mdc

    def B(N, mdcAntigo):
        mdcNovo = A(N, mdcAntigo)
        return mdcNovo

    mdc = 0
    N1 = int(input("Informe N1: "))
    N2 = int(input("Informe N2: "))

    if chose_user.upper() == "A":
        mdc = A(N1, N2)
        print("O mdc de " + str(N1) + " e " + str(N2) + " é de: " + str(mdc))
    elif chose_user.upper() == "B":
        mdcAntigo = A(N1, N2)

        continuar = True

        while continuar:
            N = int(input("Informe o valorde de N: "))

            if N == 0:
                continuar = False
            mdcLaco = B(N, mdcAntigo)
            print(str(mdcLaco) + "\n")
            mdcAntigo = mdcLaco
    else:
        print("Escolha o exercício A ou B")


####################################################################################################
def twenty_one():
    chose_user = input()

    def soma_digitos(numero):
        nun_str = str(numero)
        sum = 0

        i = 0
        while i < len(nun_str):
            sum += int(nun_str[i])
            i += 1
        return sum

    def A(n, d):
        num = int(n)

        n_digitos = 0
        ultimo = num % 10

        while num != 0:
            if d == ultimo:
                n_digitos += 1
            num = num // 10
            ultimo = num % 10
        return n_digitos

    def B(n1, n2):
        permutacao = True

        if len(n1) != len(n2) or soma_digitos(n1) != soma_digitos(n2):
            permutacao = False
        return permutacao

    permutacao = True
    if chose_user.upper() == "A":
        n = int(input())
        digito = int(input())
        quantidade_digitos = A(n, digito)
        print(quantidade_digitos)
    elif chose_user.upper() == "B":

        caracter1 = input()
        caracter2 = input()
        permutacao = B(caracter1, caracter2)

    if permutacao:
        print("Permutação")
    else:
        print("Não é permutação")


####################################################################################################
def twenty_two():
    def comprimento(n):
        i = 1
        while n != 1:
            i += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = n * 3 + 1
        return i

    N = int(input())
    i = 0
    
    while i < N:
        k = int(input())
        print(comprimento(k))
        i += 1


####################################################################################################
def twenty_three():
    print()


####################################################################################################
def twenty_four():
    char = input()

    i = 0
    j = len(char) - 1
    pali = True

    while i < j - i and pali:
        if char[i] != char[j - i]:
            pali = False

        i = i + 1

    if pali:
        print("Palindromo")
    else:
        print("Não é um palindromo")
