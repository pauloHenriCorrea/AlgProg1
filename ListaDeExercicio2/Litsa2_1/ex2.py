# Entrada de dados
birdDate = input("Informe sua data de nascimento dd/mm/aaaa: ")
currentDate = input("Informe sua data atual dd/mm/aaaa: ")


# Computação
def split(strs, sep=None):
    l = []
    cursor = ""

    for char in strs:

        if char == sep:
            l.append(int(cursor))
            cursor = ""
            continue
        cursor += char

    l.append(int(cursor))
    return l


# * dd/mm/aaaa
birdDate = split(birdDate, "/")
currentDate = split(currentDate, "/")

# * Pegando os valores do dia
birthday = birdDate[0]
currentDay = currentDate[0]

# * Pegando os valores do mês
birthMonth = birdDate[1]
currentMonth = currentDate[1]

# * Pegando os valores do ano
birthYear = birdDate[2]
currentYear = currentDate[2]

# * Calculando a idade da pessoa
if currentMonth < birthMonth:
    age = (currentYear - birthYear) - 1
elif currentMonth == birthMonth:
    if currentDay < birthday:
        age = (currentYear - birthYear) - 1
    else:
        age = currentYear - birthYear

concatenacao = "Sua idade é " + str(age)

# Saída de dados
print(concatenacao)
