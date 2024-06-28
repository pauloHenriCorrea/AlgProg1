from components.index import to_take_lines, add_CPFs_in_vetor
import os


######################################## INÍCIO DO CADASTRO ##################################################################
def check_CPF_exists(vetor_CPF, CPF):  # Verica se o CPF já está vincula a algum aluno
    i = 0
    while i < len(vetor_CPF):
        if vetor_CPF[i] == CPF:
            return True
        i += 1
    return False


def format_CPF(CPF):  # Formata o CPF
    CPF_formated = ""
    i = 0
    while i < 3:
        CPF_formated += CPF[i]
        i += 1
    CPF_formated += "."

    i = 3
    while i < 6:
        CPF_formated += CPF[i]
        i += 1
    CPF_formated += "."

    i = 6
    while i < 9:
        CPF_formated += CPF[i]
        i += 1
    CPF_formated += "-"

    i = 9
    while i < 11:
        CPF_formated += CPF[i]
        i += 1
    return CPF_formated


# Para fazer o cadastro do usuário precisamos receber o CPF e o nome do aluno
def register(route):
    if route == "student":
        lines = to_take_lines(
            "data/student_data.csv"
        )  # Pega todas a linhas do meu arquivo student_data.csv
        CPFs = add_CPFs_in_vetor(lines)

        # fp = fine point
        fp = open("data/student_data.csv", "a")

        valid = False
        while not valid:
            another_CPF = input("Informe seu CPF: ")
            if len(another_CPF) == 11:
                another_name = input("Informe seu nome: ")
                os.system("cls" if os.name == "nt" else "clear")

                lines = to_take_lines(
                    "data/student_data.csv"
                )  # Pega todas a linhas do meu arquivo student_data.csv
                CPFs = add_CPFs_in_vetor(lines)

                # Antes de adicionar os dados do aluno é necessário verificar se o CPF está vinculado a algum aluno
                exist_CPF = check_CPF_exists(CPFs, another_CPF)

                if not exist_CPF:
                    CPF_formated = format_CPF(another_CPF)
                    valid = True
                    fp.write(CPF_formated + ";" + another_name + "\n")
                    print("Aluno cadastrado com sucesso!")

                    print("\nDeseja cadrastrar outro aluno?\nSim - 1\nNão - 2")
                    response = input("Sua resposta: ")

                    match response:
                        case "1":
                            os.system("cls" if os.name == "nt" else "clear")
                            register()
                        case "2":
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Bye!")
                else:
                    print("Esté CPF está vinculado a outro aluno!")
            else:
                print("CPF inválido, por favor, digite um CPF válido")
        fp.close()
    else:
        print("Estou na rota da disciplina")


######################################## FIM DO CADASTRO #####################################################################


######################################## INICÍO DA EDIÇÃO ####################################################################
def edit(route):
    if route == "student":
        lines = to_take_lines("data/student_data.csv")
        CPF = input("Informe o CPF do aluno que deseja editar: ")

        print("O que você deseja editar?\nNome - 1\nCPF - 2")
        choise = input("Sua escolha: ")

        vector = []  # Vetor que vai receber cada linha do dados_alunos.csv
        match choise:
            case "1":
                name = input("Informe o novo nome: ")

                # Para saber qual a posição que preciso editar
                i = 0
                while i < len(lines):
                    vector.append(lines[i].split(";"))
                    if vector[i][0] == CPF:
                        vector[i][1] = "{}\n".format(name)
                    i += 1
            case "2":
                another_CPF = input("Informe o novo CPF: ")
                CPFs = add_CPFs_in_vetor(lines)
                exist = check_CPF_exists(CPFs, another_CPF)
                if not exist:
                    i = 0
                    while i < len(lines):
                        vector.append(lines[i].split(";"))
                        if vector[i][0] == CPF:
                            vector[i][0] = another_CPF
                        i += 1
        fp = open("data/student_data.csv", "w")
        i = 0
        print(vector)
        while i < len(vector):
            fp.write("{};{}".format(vector[i][0], vector[i][1]))
            i += 1
    else:
        print("Estou na rota da disciplina")
    return


######################################## FIM DA EDIÇÃO #######################################################################


######################################## INICÍO DA RAMOÇÃO ###################################################################
def remove(route):
    if route == "student":
        CPF = input("Informe o CPF do aluno que deseja remover: ")
    else:
        print("Estou na rota da disciplina")
    return


######################################## FIM DA RAMOÇÃO ######################################################################


######################################## INICÍO DA LISTAGEM ###################################################################
def to_list(route):
    if route == "student":
        linhas = to_take_lines("data/student_data.csv")

        i = 0
        data = []
        students_data = []
        while i < len(linhas):
            data.append(linhas[i].split("\n"))
            students_data.append(data[i][0].split(";"))
            i += 1

        i = 0
        while i < len(students_data):
            print("Aluno {}: ".format(i + 1))
            print("\tNome: {}".format(students_data[i][1]))
            print("\tCPF: {}".format(students_data[i][0]))
            i += 1
    else:
        print("Estou na rota da disciplina")
    return


######################################## FIM DA LISTAGEM ######################################################################
