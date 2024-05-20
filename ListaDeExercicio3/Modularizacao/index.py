from exercicios import (
    # clear,
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


##################################################################################################################################
# Define quais são os exercícios disponíveis
def opitions(option):
    option = int(option)
    if option >= 1 and option <= 24:
        # clear()
        if option == 1:
            um()
        elif option == 2:
            dois()
        elif option == 3:
            tres()
        elif option == 4:
            quatro()
        elif option == 5:
            cinco()
        elif option == 6:
            seis()
        elif option == 7:
            sete()
        elif option == 8:
            oito()
        elif option == 9:
            nove()
        elif option == 10:
            dez()
        elif option == 11:
            onze()
        elif option == 12:
            doze()
        elif option == 13:
            treze()
        elif option == 14:
            quatorze()
        elif option == 15:
            quinze()
        elif option == 16:
            dezesseis()
        elif option == 17:
            dezessete()
        elif option == 18:
            dezoito()
        elif option == 19:
            dezenove()
        elif option == 20:
            vinte()
        elif option == 21:
            vinte_e_um()
        elif option == 22:
            vinte_e_dois()
        elif option == 23:
            vinte_e_tres()
        elif option == 24:
            palindromo()
    else:
        check_entry()


##################################################################################################################################
# Talvez use mais para frente
def check_entry():
    # clear()
    print("Por favor escolha um número de exercício de 1 a 24")
    main()


##################################################################################################################################
def main():
    c = True

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
        # clear()
        c = False
        proceed(c)
    elif parans.isnumeric(): opitions(parans)
    else: check_entry()


##################################################################################################################################
def proceed(c):
    if c:
        print("Você deseja fazer outro exercício\nA) Sim\nB) Não")
        choose_user = input("Sua resposta: ")

        if choose_user.upper() == "A" or choose_user.upper() == "B":
            if choose_user.upper() == "A":
                # clear()
                print("")
            else:
                # clear()
                print("Obrigado por usar nosso programa!")
                c = False
        else:
            # clear()
            print("A sua resposta deve ser A ou B")
            proceed(c)
    else:
        # clear()
        print("Obrigado por usar nosso programa!")
    return c


restart = True  # variável de controle do laço

while restart:
    main()
    proceed(restart)
    if not proceed(restart):
        restart = False
