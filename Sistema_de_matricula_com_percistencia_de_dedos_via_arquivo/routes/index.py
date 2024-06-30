from routes.functionalities import register, edit, to_list
from components.index import (
    add_CPFs_in_vetor,
    format_CPF,
    check_CPF_or_dicipline_exists,
    to_take_lines,
)
import os


def student_options():
    os.system("cls" if os.name == "nt" else "clear")
    print("\nINFORME QUAIS DAS OPERAÇÕES ABAIXO VOCÊ DESEJA REALIZAR:\n")
    print("\t1 - CADASTRAR")
    print("\t2 - EDITAR")
    print("\t3 - REMOVER")
    print("\t4 - LISTAR")

    option = int(input())

    os.system("cls" if os.name == "nt" else "clear")
    match option:
        case 1:
            register("student")
        case 2:
            edit("student")
        case 4:
            to_list("student")
        case default:
            print("A operação inserida é inválida")


def discipline_options():
    os.system("cls" if os.name == "nt" else "clear")
    print("\nINFORME QUAIS DAS OPERAÇÕES ABAIXO VOCÊ DESEJA REALIZAR:\n")
    print("\t1 - CADASTRAR")
    print("\t2 - EDITAR")
    print("\t3 - REMOVER")
    print("\t4 - LISTAR")

    option = input()

    os.system("cls" if os.name == "nt" else "clear")
    match option:
        case "1":
            register("")
        case "2":
            edit("")
        case "4":
            to_list("")
        case default:
            print("A operação inserida é inválida")


######################################## INÍCIO DA MATRICULA DO ALUNO A UMA DISCIPLINA ########################################
def enroll_student_in_a_subject():
    CPF_valid = False
    # Pegando as linhas do arquivo de diciplinas e alunos
    lines_of_students = to_take_lines("data/students.csv")
    lines_of_diciplenes = to_take_lines("data/diciplines.csv")
    while not CPF_valid:
        CPF_student = input("INFORME O CPF DO ALUNO QUE DESEJA MATRICULAR: ")
        if len(CPF_student) == 11:
            # Verifica se o CPF informado existe
            CPFs = add_CPFs_in_vetor(lines_of_students)
            CPF_student_formated = format_CPF(CPF_student)
            exist_CPF_student = check_CPF_or_dicipline_exists(
                CPFs, CPF_student_formated
            )

            if exist_CPF_student:
                CPF_valid = True
                name_dicipline_valid = False
                while not name_dicipline_valid:
                    dicipline = input(
                        "INFORME A DISCIPLINA QUE DESEJA MATRICULAR O ALUNO: "
                    )
                    # Verifica se a disciplina informada existe
                    exist_discipline = check_CPF_or_dicipline_exists(
                        lines_of_diciplenes, dicipline.upper() + "\n"
                    )
                    if exist_discipline:
                        name_dicipline_valid = True
                        lines_of_links = to_take_lines("data/links.csv")

                        # Aqui dentro tenho que arrumar uma forma de verificar se a disciplina já existe no arquivo links.csv
                        # Se já existe adiciono o CPF desejado na linha da disciplina
                        # Se não existe adiciono uma nova linha e coloco o disciplina e o CPF
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
