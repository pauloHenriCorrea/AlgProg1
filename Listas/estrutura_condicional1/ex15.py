group = input(
    "\nInforme se o animal é do grupo:\nA) Vertebrado\nB) Invertebrado\nSua reposta: "
)

if group.upper() == "A":
    animal_class = input("\nInforme a classe: \nA) Ave\nB) Mamifero\nSua reposta: ")
    if animal_class.upper() == "A":
        type_feeding = input(
            "\nInforme o tipo de alimentação:\nA) Carnivoro\nB) Onivoro:\nSua resposta: "
        )
        if type_feeding.upper() == "A":
            print("Aguia")
        else:  # onivoro
            print("Pomba")
    else:  # mamifero
        type_feeding = input(
            "\nInforme o tipo de alimentação:\nA) Onivoro\nB) Herbivoro:\nSua resposta: "
        )
        if type_feeding.upper() == "A":
            print("Homem")
        else:  # herbivoro
            print("Vaca")
else:  # invertebrado
    animal_class = input("\nInforme se é: \nA) Inseto\nB) Anelidio\nSua reposta: ")
    if animal_class.upper() == "A":
        type_feeding = input(
            "\nInforme o tipo de alimentação:\nA) Hematofago\nB) Herbivoro:\nSua resposta: "
        )
        if type_feeding.upper() == "A":
            print("Pulga")
        else:
            print("Lagarta")
    else:
        type_feeding = input(
            "\nInforme o tipo de alimentação:\nA) Hematofago\nB) Onivoro:\nSua resposta: "
        )
        if type_feeding.upper() == "A":
            print("Sanguessuga")
        else:
            print("Minhoca")
