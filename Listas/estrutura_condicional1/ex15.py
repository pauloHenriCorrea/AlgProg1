grupo = input(
    "\nInforme se o animal é do grupo:\nA) Vertebrado\nB) Invertebrado\nSua reposta: "
)

if grupo.upper() == "A":
    classe = input("\nInforme a classe: \nA) Ave\nB) Mamifero\nSua reposta: ")
    if classe.upper() == "A":
        tipoAlimentacao = input(
            "\nInforme o tipo de alimentação:\nA) Carnivoro\nB) Onivoro:\nSua resposta: "
        )
        if tipoAlimentacao.upper() == "A":
            print("Aguia")
        else:  # onivoro
            print("Pomba")
    else:  # mamifero
        tipoAlimentacao = input(
            "\nInforme o tipo de alimentação:\nA) Onivoro\nB) Herbivoro:\nSua resposta: "
        )
        if tipoAlimentacao.upper() == "A":
            print("Homem")
        else:  # herbivoro
            print("Vaca")
else:  # invertebrado
    classe = input("\nInforme se é: \nA) Inseto\nB) Anelidio\nSua reposta: ")
    if classe.upper() == "A":
        tipoAlimentacao = input(
            "\nInforme o tipo de alimentação:\nA) Hematofago\nB) Herbivoro:\nSua resposta: "
        )
        if tipoAlimentacao.upper() == "A":
            print("Pulga")
        else:
            print("Lagarta")
    else:
        tipoAlimentacao = input(
            "\nInforme o tipo de alimentação:\nA) Hematofago\nB) Onivoro:\nSua resposta: "
        )
        if tipoAlimentacao.upper() == "A":
            print("Sanguessuga")
        else:
            print("Minhoca")
