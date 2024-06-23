# Entrada de dados
N = int(input())  # Quantidade de dias da semana

# Inicialização das variáveis
i = 0
temperaturas = []
soma = 0

# Recebe os valos dos N dias
while i < N:
    # Temperatura dos respctivos dias
    n = int(input())
    soma += n
    temperaturas.append(n)
    i += 1
m = soma / N  # Faz a média das temperaturas

# Inicializando as variáveis
c = 0  # Quantidade de temperaturas que ficaram a cima da média
i = 0

# Percorrer o vetor de temperaturas
while i < len(temperaturas):
    # Verifica quais temperaturas ficaram acima da média
    if temperaturas[i] > m:
        c += 1
    i += 1

# Saída de dados
print(m)
print(c)
