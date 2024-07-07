###############################################################################################################################################
def add_CPFs_in_vetor(lines):  # Adiciona os CPFs existentes em um vetor
    vector = []  # Vetor que vai receber cada linha do dados_alunos.csv
    CPFs = []  # Vetor que armazena todos os CPFs já cadastrado

    i = 0
    while i < len(lines):
        vector.append(lines[i].split(";"))
        CPFs.append(vector[i][0])
        i += 1
    return CPFs


###############################################################################################################################################
def to_take_lines(url):  # Pega todas as linhas do arquivo.csv
    fp = open(url, "r")
    linhas = fp.readlines()
    fp.close()
    return linhas


###############################################################################################################################################
def check_CPF_or_dicipline_exists(
    vetor, entry, function=""
):  # Verica se o CPF já está vincula a algum aluno
    if function == "remove":
        v = []
        i = 0
        while i < len(vetor):
            if vetor[i].strip() == entry:
                v.append(True)
                v.append(i)
            i += 1
        if len(v) == 0:
            v.append(False)
        return v
    else:
        i = 0
        while i < len(vetor):
            if vetor[i].strip() == entry:
                return True
            i += 1
        return False


###############################################################################################################################################
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
