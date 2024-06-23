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
