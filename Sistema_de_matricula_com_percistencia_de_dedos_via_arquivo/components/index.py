###############################################################################################################################################
# Adiciona os CPFs existentes em um vetor
def add_CPFs_in_vetor(lines):
    vector = []  # Vetor que vai receber cada linha do dados_alunos.csv
    CPFs = []  # Vetor que armazena todos os CPFs já cadastrado

    i = 0
    while i < len(lines):
        vector.append(lines[i].split(";"))
        CPFs.append(vector[i][0])
        i += 1
    return CPFs


###############################################################################################################################################
# Pega todas as linhas do arquivo alunos.csv
def to_take_lines(url):
    fp = open(url, "r")
    linhas = fp.readlines()
    fp.close()
    return linhas
