"""
Uma empresa decide dar um aumento de 30% aos funcionários com salários
inferiores a R$ 500,00. Faça um programa que recebe o salário do funcionário e
mostra o valor do salário reajustado ou uma mensagem, caso o funcionário não
tenha direito ao aumento.
"""

# Emtrada de dados
employeeSalary = float(input("Informe seu salário: "))

# Computação
# * Verificando quais funcionários possuir salários inferiores a 500,00 R$
if employeeSalary < 500:
    employeeSalary = employeeSalary + (
        employeeSalary * 0.3
    )  # * 0.3 equivale ao aumento de 30%
    print("Seu salário reajustado é de " + str(employeeSalary) + " R$")
else:
    print("Você não tem direito ao aumento no salário")
