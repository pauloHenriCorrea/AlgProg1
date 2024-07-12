from components.index import (
    to_take_lines,
    add_CPFs_in_vetor,
    check_CPF_or_dicipline_exists,
    format_CPF,
    go_back,
)

# from routes.index import student_options
import os

# Biblioteca utilizada para gerar um código aleatório
import random


######################################## FUNÇÕES AUXILIARES ##################################################################
# Gera um código aleatório com 9 digitos,
def generate_random_code():  # Talvez use essa função
    code = ""

    i = 0
    while i < 9:
        digit = random.randint(0, 9)  # Gera um dígito aleatório entre 0 e 9
        code += str(digit)
        i += 1
    return code


######################################## FUNÇÕES AUXILIARES ##################################################################

######################################## INÍCIO DO CADASTRO ##################################################################


# Para fazer o cadastro do usuário precisamos receber o CPF e o nome do aluno
def register(route=""):
    os.system("cls" if os.name == "nt" else "clear")
    if route == "student":
        valid = False
        while not valid:
            another_CPF = input("INFORME O CPF OU DIGITE 'EXIT' PARA VOLTAR: ").upper()

            if go_back(another_CPF):
                return True

            if len(another_CPF) == 11 and another_CPF.isnumeric():
                lines = to_take_lines(
                    "data/students.csv"
                )  # Pega todas a linhas do meu arquivo student_data.csv
                CPFs = add_CPFs_in_vetor(lines)
                CPF_formated = format_CPF(another_CPF)
                exist_CPF = check_CPF_or_dicipline_exists(CPFs, CPF_formated)

                # Antes de adicionar os dados do aluno é necessário verificar se o CPF está vinculado a algum aluno
                if not exist_CPF:
                    another_name = input("INFORME O NOME: ")
                    os.system("cls" if os.name == "nt" else "clear")

                    valid = True

                    # fp = fine point
                    fp = open("data/students.csv", "a")
                    fp.write("{};{}\n".format(CPF_formated, another_name.upper()))
                    fp.close()

                    print("ALUNO CADASTRADO COM SUCESSO!")
                else:
                    print("ESTÉ CPF ESTÁ VINCULADO A OUTRO ALUNO!")
            else:
                print("CPF INVÁLIDO, POR FAVOR, DIGITE UM CPF VÁLIDO")
    else:
        valid = False
        while not valid:
            name_dicipline = input(
                "INFORME O NOME DA DISCIPLINA OU DIGITE 'EXIT' PARA VOLTAR: "
            ).upper()

            if go_back(name_dicipline):
                return True

            if (
                name_dicipline
                and not name_dicipline.isnumeric()
                and name_dicipline != "EXIT"
            ):
                lines = to_take_lines("data/diciplines.csv")
                exist = check_CPF_or_dicipline_exists(lines, name_dicipline)

                if not exist:
                    valid = True

                    fp = open("data/diciplines.csv", "a")
                    fp.write("{}\n".format(name_dicipline))
                    fp.close()
                    print("DISCIPLINA CADASTRADA COM SUCESSO!")
                else:

                    print("ESSA DISCIPLINA JÁ ESTÁ CADASTRADA!")
            else:
                os.system("cls")
                print(
                    "ENTRADA INVÁLIDA!POSSÉVEIS ERROS:\n\tA ENTRADA É VAZIA OU A ENTRDA É UM VALOR NÚMERICO"
                )
                print(
                    "\tPOR FAVOR, INSIRA UMA DISCIPLINA VÁLIDA OU INFORME UMA ENTRADA QUE NÃO SEJA NÚMERICA\n"
                )


######################################## FIM DO CADASTRO #####################################################################


######################################## INICÍO DA EDIÇÃO ####################################################################
def edit(route=""):
    if route == "student":
        CPF_valid = False
        lines = to_take_lines("data/students.csv")
        CPFs = add_CPFs_in_vetor(lines)  # Vetor de CPFs que já foram cadastrados

        if len(CPFs) > 0:
            while not CPF_valid:
                CPF = input(
                    "DIGITE 'EXIT' PARA VOLTAR OU INFORME O CPF DO ALUNO QUE DESEJA EDITAR: "
                ).upper()

                if go_back(CPF):
                    return True

                os.system("cls" if os.name == "nt" else "clear")
                # Verificação se o CPF tem 11 digitos
                if len(CPF) == 11:
                    CPF_formated = format_CPF(CPF)  # CPF formatado
                    exist = check_CPF_or_dicipline_exists(CPFs, CPF_formated)

                    # Verificando se o CPF existe
                    if exist:
                        CPF_valid = True
                        os.system("cls" if os.name == "nt" else "clear")
                        print(
                            "O QUE VOCÊ DESEJA EDITAR?\nNOME - 1\nCPF - 2\nNOME E CPF - 3"
                        )
                        choise = input("SUA ESCOLHA: ")

                        vector = (
                            []
                        )  # Vetor que vai receber cada linha do dados_alunos.csv

                        os.system("cls" if os.name == "nt" else "clear")
                        match choise:
                            case "1":

                                new_name = input("INFORME O NOVO NOME: ").upper()

                                # Para saber qual a posição que preciso editar
                                i = 0
                                while i < len(lines):
                                    vector.append(lines[i].split(";"))
                                    if vector[i][0] == CPF_formated:
                                        vector[i][1] = "{}\n".format(new_name)
                                    i += 1
                            case "2":
                                CPF_edit = False
                                while not CPF_edit:
                                    new_CPF = input("INFORME O NOVO CPF: ")
                                    new_CPF_formated = format_CPF(new_CPF)

                                    exist = check_CPF_or_dicipline_exists(
                                        CPFs, new_CPF_formated
                                    )

                                    if not exist:
                                        CPF_edit = True
                                        i = 0
                                        while i < len(lines):
                                            vector.append(lines[i].split(";"))
                                            if vector[i][0] == CPF_formated:
                                                vector[i][0] = new_CPF_formated
                                            i += 1
                                    else:
                                        print(
                                            "O CPF INFORMADO ESTA VINCULADO A UM ALUNO! POR FAVOR, INFORME NOVAMENTE O CPF."
                                        )
                            case "3":
                                CPF_edit = False
                                while not CPF_edit:
                                    new_CPF = input("INFORME O NOVO CPF: ")
                                    new_CPF_formated = format_CPF(new_CPF)
                                    exist = check_CPF_or_dicipline_exists(
                                        CPFs, new_CPF_formated
                                    )
                                    if not exist:
                                        CPF_edit = True
                                        new_name = input(
                                            "INFORME O NOVO NOME: "
                                        ).upper()
                                        i = 0
                                        while i < len(lines):
                                            vector.append(lines[i].split(";"))
                                            if vector[i][0] == CPF_formated:
                                                vector[i][0] = new_CPF_formated
                                                vector[i][1] = "{}\n".format(new_name)
                                            i += 1
                                    else:
                                        print(
                                            "O CPF INFORMADO ESTA VINCULADO A UM ALUNO! POR FAVOR, INFORME NOVAMENTE O CPF."
                                        )

                        fp = open("data/students.csv", "w")
                        i = 0

                        # Adiciona os dados editados
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
            os.system("cls" if os.name == "nt" else "clear")
            print("AINDA NÃO EXISTE NENHUM ALUNO CADASTRADO NO MOMENTO")
            return True
    else:

        lines = to_take_lines("data/diciplines.csv")

        stop = False
        if len(lines) > 0:
            while not stop:
                name_dicipline = input(
                    "DIGITE 'EXIT' PARA VOLTAR OU INFORME O NOME DA DISCIPLINA QUE DESEJA EDITAR: "
                ).upper()

                if go_back(name_dicipline):
                    return True

                exist = check_CPF_or_dicipline_exists(lines, name_dicipline)
                if exist:
                    stop = True
                    valid = False
                    while not valid:
                        new_name_dicipline = input(
                            "INFORME O NOVO NOME DA DISCIPLINA: "
                        ).upper()
                        if new_name_dicipline and not new_name_dicipline.isnumeric():
                            valid = True
                            i = 0
                            while i < len(lines):
                                if lines[i].strip() == name_dicipline:
                                    lines[i] = new_name_dicipline + "\n"
                                i += 1

                            fp = open("data/diciplines.csv", "w")
                            i = 0
                            while i < len(lines):
                                fp.write("{}".format(lines[i]))
                                i += 1
                            fp.close()
                        else:
                            os.system("cls")
                            print(
                                "ENTRADA INVÁLIDA!POSSÉVEIS ERROS:\n\tA ENTRADA É VAZIA OU A ENTRDA É UM VALOR NÚMERICO"
                            )
                            print(
                                "\tPOR FAVOR, INSIRA UMA DISCIPLINA VÁLIDA OU INFORME UMA ENTRADA QUE NÃO SEJA NÚMERICA\n"
                            )
                else:
                    print(
                        "A DISCUPLINA NÃO EXISTE OU É INVÁLIDA. POR FAVOR, INFORME NOVAMENTE O NOME DA DISCIPLINA"
                    )
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("NÃO EXISTE NEHUMA DISCIPLINA CADASTRADA NO MOMENTO")
            return True


######################################## FIM DA EDIÇÃO #######################################################################


######################################## INICÍO DA REMOÇÃO ###################################################################
def remove(route=""):
    if route == "student":
        CPF_valid = False
        lines = to_take_lines("data/students.csv")
        CPFs = add_CPFs_in_vetor(lines)
        if len(CPFs) > 0:
            while not CPF_valid:
                CPF = input(
                    "DIGITE 'EXIT' PARA VOLTAR OU INFORME O CPF DO ALUNO QUE DESEJA REMOVER: "
                )

                if go_back(CPF):
                    return True

                if len(CPF) == 11:
                    CPF_formated = format_CPF(CPF)

                    exist_CPF = check_CPF_or_dicipline_exists(
                        CPFs, CPF_formated, "remove"
                    )

                    if exist_CPF[0]:
                        i = 0
                        fp = open("data/students.csv", "w")
                        while i < len(lines):
                            if lines[i] != lines[exist_CPF[1]]:
                                fp.write("{}".format(lines[i]))
                            i += 1
                        fp.close()
                        CPF_valid = True

                else:
                    print(
                        "O CPF INFORMADO NÃO EXISTE OU É INVÁLIDO! POR FAVOR, INFORME NOVAMENTE O CPF."
                    )

        else:
            print("AINDA NÃO EXISTE NENHUM ALUNO CADASTRADO NO MOMENTO")
            CPF_valid = True
            return False
    else:
        diciplines = to_take_lines("data/diciplines.csv")
        if len(diciplines) > 0:
            dicipline_valid = False
            while not dicipline_valid:
                name_dicipline = input(
                    "INFORME O NOME DA DISCIPLINA QUE DESEJA REMOVER OU DIGITE 'EXIT' PARA VOLTAR: "
                ).upper()

                if go_back(name_dicipline):
                    return True

                exist = check_CPF_or_dicipline_exists(
                    diciplines, name_dicipline, "remove"
                )
                if exist[0]:
                    i = 0
                    fp = open("data/diciplines.csv", "w")
                    while i < len(diciplines):
                        if diciplines[i] != diciplines[exist[1]]:
                            fp.write(diciplines[i])
                        i += 1
                    fp.close()
                    print("DISCIPLINA REMOVIDA COM SUCESSO!")
                    return
                else:
                    print(
                        "A DISCUPLINA NÃO EXISTE OU É INVÁLIDA. POR FAVOR, INFORME NOVAMENTE O NOME DA DISCIPLINA"
                    )
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("NENHUMA DISCIPLICA CADASTRADA NO MOMENTO!")
            return True

    return


######################################## FIM DA REMOÇÃO ######################################################################


######################################## INICÍO DA LISTAGEM ###################################################################
def to_list(route=""):
    if route == "student":
        lines = to_take_lines("data/students.csv")
        if len(lines) > 0:
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
            print("NENHUM ALUNO CADASTRADO NO MOMENTO")
    else:
        lines = to_take_lines("data/diciplines.csv")
        if len(lines) > 0:
            i = 0
            while i < len(lines):
                print("DISCIPLINA {}: {}".format(i + 1, lines[i]))
                i += 1
        else:
            print("NEHUMA DISCIPLINA CADASTRADA NO MOMENTO")

    return


######################################## FIM DA LISTAGEM ######################################################################
