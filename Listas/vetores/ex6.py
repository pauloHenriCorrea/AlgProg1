grau_polinomio = int(input("Informe o valor do grau do polinomio: "))


def coeficiente_real(grau):
    grau += 1
    coeficientes = [0] * grau
    i = 0
    while i < grau + 1:
        coeficiente = int(input("informe o valor de a" + str(i) + ": "))
        coeficientes[i] += coeficiente
        i += 1
    return coeficientes


def pontos_do_polinomio(grau):
    grau += 1
    pontos = [0] * grau
    i = 0
    while i < grau + 1:
        ponto = int(input("informe o valor de x" + str(i) + ": "))
        pontos[i] += ponto
        i += 1
    return pontos


i = 0
soma = 0

coeficientes = coeficiente_real(grau_polinomio)
# pontos = pontos_do_polinomio(grau_polinomio)
x = int(input("Informe o valor de x: "))
while i < grau_polinomio + 1:
    soma += coeficientes[i] * (x**i)
    i += 1
print(soma)
