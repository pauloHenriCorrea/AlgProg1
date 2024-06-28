from students.index import student_options
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

print("\nINFORME QUAIS DAS OPERAÇÕES ABAIXO VOCÊ DESEJA REALIZAR:\n")
print("\t1 - CADASTRAR, EDITAR, REMOVER OU LISTAR ALUNO")
print("\t2 - CADASTRAR, EDITAR, REMOVER OU LISTAR DISCIPLINA")
print("\t3 - MATRICULAR ALUNO EM UMA DISCIPLINA")
print("\t4 - CANCELAR MATRICULA DE UM ESTUDANTE")
print("\t5 - RELATÓRIO\n")

option = int(input())

match option:
    case 1:
        os.system("cls" if os.name == "nt" else "clear")
        student_options()

    case default:
        print("A operação inserida é inválida")
