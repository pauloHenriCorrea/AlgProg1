from routes.index import (
    student_options,
    discipline_options,
    enroll_student_in_a_subject,
)
import os

"""
* Desenvolver um sistema que permite as seguintes operações:
    => 1 - Cadastrar, editar, remover e listar alunos;
        ° Cada aluno deve ter: CPF (cada CPF só poderá está associado a somente um aluno) e nome;
    
    => 2 - Cadastar, editar, remover, e listar disciplina;
        ° Cada disciplina deve ter: nome;
    
    => 3 - Matricular aluno em uma disciplina;

    => 4 - Cancelar matricula de um estudante;

    => 5 - Relatório de maticula por disciplina contendo nome da disciplina e nome dos alunos matriculado;

    => 6 - Sair
"""


def menu():
    print("\nINFORME QUAIS DAS OPERAÇÕES ABAIXO VOCÊ DESEJA REALIZAR:\n")
    print("\t1 - CADASTRAR, EDITAR, REMOVER OU LISTAR ALUNO")
    print("\t2 - CADASTRAR, EDITAR, REMOVER OU LISTAR DISCIPLINA")
    print("\t3 - MATRICULAR ALUNO EM UMA DISCIPLINA")
    print("\t4 - CANCELAR MATRICULA DE UM ESTUDANTE")
    print("\t5 - RELATÓRIO")
    print("\t6 - SAIR\n")

    option = input()

    os.system("cls" if os.name == "nt" else "clear")
    match option:
        case "1":
            student_options()
        case "2":
            discipline_options()
        case "3":
            enroll_student_in_a_subject()
        case "6":
            return True
        case default:
            print(
                "O NÚMERO INSERIDO NÃO CORRESPONDE A NENHUMA DAS OPERAÇÃO EXISTENTES."
            )
            print("POR FAVOR, DIGITE UM NÚMERO DE OPERAÇÃO VÁLIDO")


def main():
    stop = False
    while not stop:
        if menu():
            stop = True


main()
