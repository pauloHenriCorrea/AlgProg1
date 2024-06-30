from components.index import to_take_lines, add_CPFs_in_vetor
import os

# Biblioteca utilizada para gerar um código aleatório
import random


######################################## FUNÇÕES AUXILIARES ##################################################################
def check_CPF_or_dicipline_exists(
    vetor, entry
):  # Verica se o CPF já está vincula a algum aluno
    i = 0
    while i < len(vetor):
        if vetor[i] == entry:
            return True
        i += 1
    return False


# Gera um código aleatório com 9 digitos,
def generate_random_code():  # Talvez use essa função
    code = ""

    i = 0
    while i < 9:
        digit = random.randint(0, 9)  # Gera um dígito aleatório entre 0 e 9
        code += str(digit)
        i += 1
    return code


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


######################################## FUNÇÕES AUXILIARES ##################################################################

######################################## INÍCIO DO CADASTRO ##################################################################


# Para fazer o cadastro do usuário precisamos receber o CPF e o nome do aluno
def register(route):
    if route == "student":
        valid = False
        while not valid:
            another_CPF = input("INFORME O CPF: ")
            if len(another_CPF) == 11:
                another_name = input("INFORME O NOME: ")
                os.system("cls" if os.name == "nt" else "clear")

                lines = to_take_lines(
                    "data/students.csv"
                )  # Pega todas a linhas do meu arquivo student_data.csv
                CPFs = add_CPFs_in_vetor(lines)

                # Antes de adicionar os dados do aluno é necessário verificar se o CPF está vinculado a algum aluno
                exist_CPF = check_CPF_or_dicipline_exists(CPFs, another_CPF)

                if not exist_CPF:
                    # fp = fine point
                    fp = open("data/students.csv", "a")

                    CPF_formated = format_CPF(another_CPF)
                    valid = True
                    fp.write("{};{}\n".format(CPF_formated, another_name.upper()))
                    print("ALUNO CADASTRADO COM SUCESSO!")

                    # Dqui para baixo dá erro caso o usuário digitar o mesmo cpf mais de uma vez durante a execução do programa, ele salva o mesmo cpf para usuário diferestes
                    print("\nDESEJA CADASTRAR OUTRO ALUNO?\nSIM - 1\nNÃO - 2")
                    response = input("SUA RESPOSTA: ")

                    match response:
                        case "1":
                            os.system("cls" if os.name == "nt" else "clear")
                            register("student")
                        case "2":
                            os.system("cls" if os.name == "nt" else "clear")
                            # student_options()
                else:
                    print("ESTÉ CPF ESTÁ VINCULADO A OUTRO ALUNO!")
            else:
                print("CPF INVÁLIDO, POR FAVOR, DIGITE UM CPF VÁLIDO")
        fp.close()
    else:
        valid = False
        while not valid:
            name_dicipline = input("INFORME O NOME DA DISCIPLINA: ")

            lines = to_take_lines("data/diciplines.csv")
            exist = check_CPF_or_dicipline_exists(lines, name_dicipline + "\n")

            if not exist:
                fp = open("data/diciplines.csv", "a")
                fp.write("{}\n".format(name_dicipline.upper()))
                fp.close()
                valid = True
                print("DISCIPLINA CADASTRADA COM SUCESSO!")
            else:

                print("ESSA DISCIPLINA JÁ ESTÁ CADASTRADA!")


######################################## FIM DO CADASTRO #####################################################################


######################################## INICÍO DA EDIÇÃO ####################################################################
def edit(route):
    if route == "student":
        CPF = input("INFORME O CPF DO ALUNO QUE DESEJA EDITAR: ")
        if len(CPF) == 11:

            lines = to_take_lines("data/students.csv")
            CPFs = add_CPFs_in_vetor(lines)
            CPF_formated = format_CPF(CPF)
            exist = check_CPF_or_dicipline_exists(CPFs, CPF_formated)

            if exist:
                os.system("cls" if os.name == "nt" else "clear")
                print("O QUE VOCÊ DESEJA EDITAR?\nNOME - 1\nCPF - 2\nNOME E CPF - 3")
                choise = input("SUA ESCOLHA: ")

                vector = []  # Vetor que vai receber cada linha do dados_alunos.csv

                os.system("cls" if os.name == "nt" else "clear")
                match choise:
                    case "1":

                        new_name = input("INFORME O NOVO NOME: ")

                        # Para saber qual a posição que preciso editar
                        i = 0
                        while i < len(lines):
                            vector.append(lines[i].split(";"))
                            if vector[i][0] == CPF_formated:
                                vector[i][1] = "{}\n".format(new_name.upper())
                            i += 1

                    case "2":

                        new_CPF = input("INFORME O NOVO CPF: ")
                        new_CPF_formated = format_CPF(new_CPF)

                        CPFs = add_CPFs_in_vetor(lines)

                        exist = check_CPF_or_dicipline_exists(CPFs, new_CPF_formated)

                        if not exist:
                            i = 0
                            while i < len(lines):
                                vector.append(lines[i].split(";"))
                                if vector[i][0] == CPF_formated:
                                    vector[i][0] = new_CPF_formated
                                i += 1
                    case "3":
                        new_CPF = input("INFORME O NOVO CPF: ")
                        new_name = input("INFORME O NOVO NOME: ")

                        new_CPF_formated = format_CPF(new_CPF)

                        CPFs = add_CPFs_in_vetor(lines)

                        exist = check_CPF_or_dicipline_exists(CPFs, new_CPF_formated)
                        if not exist:
                            i = 0
                            while i < len(lines):
                                vector.append(lines[i].split(";"))
                                if vector[i][0] == CPF_formated:
                                    vector[i][0] = new_CPF_formated
                                    vector[i][1] = "{}\n".format(new_name.upper())
                                i += 1

                fp = open("data/students.csv", "w")
                i = 0
                while i < len(vector):
                    fp.write("{};{}".format(vector[i][0], vector[i][1]))
                    i += 1
                fp.close()
            else:
                print(
                    "O CPF INFORMADO NÃO EXISTE OU É INVÁLIDO! POR FAVOR, INFORME NOVAMENTE O CPF."
                )
        else:
            print(
                "O CPF INFORMADO NÃO EXISTE OU É INVÁLIDO! POR FAVOR, INFORME NOVAMENTE O CPF."
            )
    else:
        lines = to_take_lines("data/diciplines.csv")
        name_dicipline = input("INFORME O NOME DA DISCIPLINA QUE DESEJA EDITAR: ")

        i = 0
        while i < len(lines):
            if lines[i] == name_dicipline + "\n":
                new_name_dicipline = input("INFORME O NOME NOME DA DISCIPLINA")
                lines[i] = new_name_dicipline
            i += 1
        fp = open("data/diciplines.csv", "w")
        i = 0
        while i < len(lines):
            fp.write("{}\n".format(lines[i]))
            i += 1
        fp.close()


######################################## FIM DA EDIÇÃO #######################################################################


######################################## INICÍO DA RAMOÇÃO ###################################################################
def remove(route):
    if route == "student":
        CPF = input("INFORME O CPF DO ALUNO QUE DESEJA REMOVER: ")
    else:
        print("Estou na rota da disciplina")
    return


######################################## FIM DA RAMOÇÃO ######################################################################


######################################## INICÍO DA LISTAGEM ###################################################################
def to_list(route):
    if route == "student":
        lines = to_take_lines("data/students.csv")

        data = []
        i = 0
        students_data = []
        while i < len(lines):
            data.append(lines[i].split("\n"))
            students_data.append(data[i][0].split(";"))
            i += 1

        i = 0
        while i < len(students_data):
            print("ALUNO {}: ".format(i + 1))
            print("\tNOME: {}".format(students_data[i][1]))
            print("\tCPF: {}".format(students_data[i][0]))
            i += 1
    else:
        lines = to_take_lines("data/diciplines.csv")

        i = 0
        while i < len(lines):
            print("DISCIPLINA {}: {}".format(i + 1, lines[i]))
            i += 1

    return


######################################## FIM DA LISTAGEM ######################################################################
