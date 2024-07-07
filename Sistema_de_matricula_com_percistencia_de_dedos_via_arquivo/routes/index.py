# Operações básicas
from routes.functionalities import register, edit, to_list, remove

# Funções auxíliares
from components.index import (
    add_CPFs_in_vetor,
    format_CPF,
    check_CPF_or_dicipline_exists,
    to_take_lines,
)
import os


######################################## FUNÇÃO PARA REPETIR UMA OPERAÇÃO ENQUANTO O USUÁRIO QUISER ###########################
def repeat(
    function,
    menu,
    to_list,
    message,
    route="",
):
    stop = False
    while not stop:
        to_list(route)
        msg = "OUTRO ALUNO" if route == "student" else "OUTRA DISCIPLINA"
        if function(route) == None:
            print("\nDESEJA {} {}?\nSIM - 1\nNÃO - 2".format(message, msg))
            response = input("SUA RESPOSTA: ")
            os.system("cls" if os.name == "nt" else "clear")
            if response == "2":
                stop = True
                menu()
        else:
            stop = True
            menu()


def student_options():
    print("\nINFORME QUAIS DAS OPERAÇÕES ABAIXO VOCÊ DESEJA REALIZAR:\n")
    print("\t1 - CADASTRAR")
    print("\t2 - EDITAR")
    print("\t3 - REMOVER")
    print("\t4 - LISTAR")
    print("\t5 - VOLTAR")

    option = input()

    match option:
        case "1":
            os.system("cls" if os.name == "nt" else "clear")
            repeat(register, student_options, to_list, "CADASTRAR", "student")
        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            repeat(edit, student_options, to_list, "EDITAR", "student")
        case "3":
            os.system("cls" if os.name == "nt" else "clear")
            repeat(remove, student_options, to_list, "REMOVER", "student")
        case "4":
            os.system("cls" if os.name == "nt" else "clear")
            to_list("student")
            student_options()
        case "5":
            os.system("cls" if os.name == "nt" else "clear")
            return
        case default:
            os.system("cls" if os.name == "nt" else "clear")
            print("A OPERAÇÃO INSERIDA É INVÁLIDA")
            student_options()


def discipline_options():
    print("\nINFORME QUAIS DAS OPERAÇÕES ABAIXO VOCÊ DESEJA REALIZAR:\n")
    print("\t1 - CADASTRAR")
    print("\t2 - EDITAR")
    print("\t3 - REMOVER")
    print("\t4 - LISTAR")
    print("\t5 - VOLTAR")

    option = input()

    match option:
        case "1":
            os.system("cls" if os.name == "nt" else "clear")
            repeat(register, discipline_options, to_list, "CADASTRAR")
        case "2":
            os.system("cls" if os.name == "nt" else "clear")
            repeat(edit, discipline_options, to_list, "EDITAR")
        case "3":
            os.system("cls" if os.name == "nt" else "clear")
            repeat(remove, discipline_options, to_list, "REMOVER")
        case "4":
            os.system("cls" if os.name == "nt" else "clear")
            to_list()
            discipline_options()
        case "5":
            os.system("cls" if os.name == "nt" else "clear")
            return
        case default:
            os.system("cls" if os.name == "nt" else "clear")
            print("A OPERAÇÃO INSERIDA É INVÁLIDA")
            discipline_options()


######################################## INÍCIO DA MATRICULA DO ALUNO A UMA DISCIPLINA ########################################
def enroll_student_in_a_subject():
    CPF_valid = False
    # Pegando as linhas do arquivo de diciplinas e alunos
    lines_of_students = to_take_lines("data/students.csv")
    lines_of_diciplenes = to_take_lines("data/diciplines.csv")

    while not CPF_valid:
        CPF_student = input("INFORME O CPF DO ALUNO QUE DESEJA MATRICULAR: ")

        # Verifica se o CPF é válido
        if len(CPF_student) == 11:
            CPFs = add_CPFs_in_vetor(lines_of_students)
            CPF_student_formated = format_CPF(CPF_student)
            exist_CPF_student = check_CPF_or_dicipline_exists(
                CPFs, CPF_student_formated
            )

            # Verifica se o CPF esta vinculado a algum estudante
            if exist_CPF_student:
                CPF_valid = True
                name_dicipline_valid = False

                # Equanto o usuário não digitar um nome de uma disciplina que existe ele ficará em um laço infinito
                while not name_dicipline_valid:
                    dicipline = input(
                        "INFORME A DISCIPLINA QUE DESEJA MATRICULAR O ALUNO: "
                    ).upper()

                    # Verifica se a disciplina informada existe
                    exist_discipline = check_CPF_or_dicipline_exists(
                        lines_of_diciplenes, dicipline.upper() + "\n"
                    )

                    if exist_discipline:
                        name_dicipline_valid = True

                        lines_of_links = to_take_lines(
                            "data/links.csv"
                        )  # Pega todos os vinculos de alunos e disciplinas

                        datas = []  # para tirar o "\n"
                        lines = []  # para tirar o "":"

                        # para quebrar a linha em um vetor em que a primeira posição seja as discplinas e a segunda seja os cpf
                        links = []
                        diciplines = []  # pega todas as diciplinas
                        students = []  # para tirar a virgula links[i][1]
                        CPFs_students = []  # para pegar todos os CPFs

                        i = 0
                        while i < len(lines_of_links):
                            datas.append(lines_of_links[i].split("\n"))
                            print("\nDATAS: {}\n".format(datas))

                            lines.append(datas[i][0])
                            print("\nLINES: {}\n".format(lines))

                            links.append(lines[i].split(":"))
                            print("\nLINKS: {}\n".format(links))

                            diciplines.append(links[i][0])
                            print("\nDICIPLINES: {}\n".format(diciplines))

                            students.append(links[i][1].split(","))
                            print("\nSTUDENTS: {}\n".format(students))

                            # Talvez não precise dessa parte
                            # j = 0
                            # while j < len(students[i]):
                            #     CPFs_students.append(students[i][j])
                            #     j += 1
                            i += 1
                            # print("\nCPFS: {}\n".format(CPFs_students))

                        # Aqui dentro tenho que arrumar uma forma de verificar se a disciplina já existe no arquivo links.csv ok
                        exist_dicipline_in_links = check_CPF_or_dicipline_exists(
                            diciplines, dicipline
                        )

                        """
                        Daqui para baixo não vai funcionar
                        # Se não existe adiciono uma nova linha e coloco o disciplina e o CPF
                        fp = open("data/links.csv", "a")
                        if not exist_dicipline_in_links:
                            fp.write(
                                "{}:{}\n".format(
                                    dicipline.upper(), CPF_student_formated
                                )
                            )
                        else:
                            # Se a disciplina já existe, verifico se o CPF já vinculado a ela
                            exist_CPF_in_dicipline = check_CPF_or_dicipline_exists(
                                CPFs_students, CPF_student_formated
                            )

                            if not exist_CPF_in_dicipline:
                                print(CPFs_students)
                                CPFs_students.append(CPF_student_formated)
                                print(CPFs_students)
                        """
                    else:
                        print(
                            "A DISCUPLINA NÃO EXISTE OU É INVÁLIDA. POR FAVOR, INFORME NOVAMENTE O NOME DA DISCIPLINA"
                        )
            else:
                print(
                    "O CPF INFORMADO NÃO EXISTE OU É INVÁLIDO! POR FAVOR, INFORME NOVAMENTE O CPF."
                )
        else:
            print(
                "O CPF INFORMADO NÃO EXISTE OU É INVÁLIDO! POR FAVOR, INFORME NOVAMENTE O CPF."
            )


######################################## FIM DA MATRICULA DO ALUNO A UMA DISCIPLINA ###########################################
