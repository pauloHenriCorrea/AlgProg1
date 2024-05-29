from exercicios import (
    clear,
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    ten,
    eleven,
    twelven,
    thirteen,
    fourteen,
    fifteen,
    sixteen,
    seventeen,
    eighteen,
    nineteen,
    twenty,
    twenty_one,
    twenty_two,
    twenty_three,
    twenty_four,
)


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
        clear()
        c = False
        proceed(c)
    elif parans.isnumeric():
        opitions(parans)
    else:
        check_entry()
    return c


##################################################################################################################################
# Define quais são os exercícios disponíveis
def opitions(option):
    option = int(option)
    if option >= 1 and option <= 24:
        clear()
        if option == 1:
            one()
        elif option == 2:
            two()
        elif option == 3:
            three()
        elif option == 4:
            four()
        elif option == 5:
            five()
        elif option == 6:
            six()
        elif option == 7:
            seven()
        elif option == 8:
            eight()
        elif option == 9:
            nine()
        elif option == 10:
            ten()
        elif option == 11:
            eleven()
        elif option == 12:
            twelven()
        elif option == 13:
            thirteen()
        elif option == 14:
            fourteen()
        elif option == 15:
            fifteen()
        elif option == 16:
            sixteen()
        elif option == 17:
            seventeen()
        elif option == 18:
            eighteen()
        elif option == 19:
            nineteen()
        elif option == 20:
            twenty()
        elif option == 21:
            twenty_one()
        elif option == 22:
            twenty_two()
        elif option == 23:
            twenty_three()
        elif option == 24:
            twenty_four()
    else:
        check_entry()


##################################################################################################################################
# Talvez use mais para frente
def check_entry():
    clear()
    print("Por favor escolha um número de exercício de 1 a 24")
    main()


##################################################################################################################################
def proceed(c):
    if c:
        print("Você deseja fazer outro exercício\nA) Sim\nB) Não")
        choose_user = input("Sua resposta: ")

        if choose_user.upper() == "A" or choose_user.upper() == "B":
            if choose_user.upper() == "A":
                clear()
                print("")
            else:
                clear()
                print("Obrigado por usar nosso programa!")
                c = False
        else:
            clear()
            print("A sua resposta deve ser A ou B")
            proceed(c)
    else:
        clear()
        print("Obrigado por usar nosso programa!")
    return c


restart = True  # variável de controle do laço

while restart:
    if main():
        if not proceed(restart):
            restart = False
    else:
        restart = False
