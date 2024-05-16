from Modularizacao.exercicios import (
    clear,
    um,
    dois,
    tres,
    quatro,
    cinco,
    seis,
    sete,
    oito,
    nove,
    dez,
    onze,
    doze,
    treze,
    quatorze,
    quinze,
    dezesseis,
    dezessete,
    dezoito,
    dezenove,
    vinte,
    vinte_e_um,
    vinte_e_dois,
    vinte_e_tres,
    palindromo,
)


continuar = True


def main():

    def verificarEntrada():
        clear()
        print("Por favor escolha um número de exercício de 1 a 23")
        main()

    print(
        "_____________________________________________________________________________________________________"
    )
    print(
        "\n\n     Informe abaixo, qual exercício você deseja executar ou digite exit para encerrar o programa\n"
    )
    print(
        "_____________________________________________________________________________________________________\n"
    )

    # Variável utilizada para pegar o número do exercício que o usuário quer
    parans = input()

    if parans == "exit":
        clear()
        global continuar
        continuar = False
    elif parans.isnumeric():
        parans = int(parans)
        if parans >= 1 and parans <= 24:
            clear()
            if parans == 1:
                um()
            elif parans == 2:
                dois()
            elif parans == 3:
                tres()
            elif parans == 4:
                quatro()
            elif parans == 5:
                cinco()
            elif parans == 6:
                seis()
            elif parans == 7:
                sete()
            elif parans == 8:
                oito()
            elif parans == 9:
                nove()
            elif parans == 10:
                dez()
            elif parans == 11:
                onze()
            elif parans == 12:
                doze()
            elif parans == 13:
                treze()
            elif parans == 14:
                quatorze()
            elif parans == 15:
                quinze()
            elif parans == 16:
                dezesseis()
            elif parans == 17:
                dezessete()
            elif parans == 18:
                dezoito()
            elif parans == 19:
                dezenove()
            elif parans == 20:
                vinte()
            elif parans == 21:
                vinte_e_um()
            elif parans == 22:
                vinte_e_dois()
            elif parans == 23:
                vinte_e_tres()
            elif parans == 24:
                palindromo()
        else:
            verificarEntrada()
    else:
        verificarEntrada()


def parar():

    global continuar

    if continuar:
        print("Você deseja fazer outro exercício\nA) Sim\nB) Não")
        x = input("Sua resposta: ")

        if x.upper() == "A" or x.upper() == "B":
            if x.upper() == "A":
                clear()
            else:
                clear()
                print("Obrigado por usar nosso programa!")
                continuar = False
        else:
            clear()
            print("A sua resposta deve ser A ou B")
            parar()
    else:
        print("Obrigado por usar nosso programa!")


while continuar:
    main()
    parar()
