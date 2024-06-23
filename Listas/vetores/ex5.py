# Observação: na roleta pode sair números em um intervalo de 0 - 36.
def le_numeros(n):
    numeros = []
    i = 0
    while i < n:
        # Número que saiu na roleta
        numero = int(input())
        # Verifica se o número informado está em um intervalo válido
        if numero >= 0 and numero <= 36:
            numeros.append(numero)
            i += 1
        else:
            print("Valor inválido! Informe novamente.")
    return numeros


n = int(input())
valores = le_numeros(n)

# Declarando vetor, e definindo com 37 posicoes
numeros = [0] * 37

i = 0
# Adicina a quantidade de vezes que o determinado número inserio pelo usuário saiu
while i < n:
    numeros[valores[i]] += 1
    i += 1

# Saída de dados
print(numeros)
