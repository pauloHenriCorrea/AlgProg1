from students.functionalities import register, edit, to_list
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
            register()
        case 2:
            edit()
        case 4:
            to_list()
        case default:
            print("A operação inserida é inválida")
