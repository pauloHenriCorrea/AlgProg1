"""
1. Polinômios são usados em uma ampla variedade de áreas da Matemática e das
Ciências. Um polinômio é uma expressão de comprimento finito construída
a partir de variáveis e constantes, usando apenas as operações de adição, 
subtração, multiplicação e expoentes não-negativos. Por exemplo, x³ + x² - 8 
é um polinômio.
Uma função polinomial é uma função que pode ser definida pela avaliação de
um polinômio. Uma função f, de um único argumento, é chamada uma função
polinomial se satisfaz:
f(x) = an.xⁿ + an - 1x^^n - 1 + · · · + a2x² + a1x + a0

para qualquer x, onde n é um número inteiro não-negativo e a0, a1, . . . , an são
coeficientes constantes.

Por exemplo, a função f: Z → Z definida por

f(x) = x³ + x² - 8

é uma função polinomial de um argumento (x). Escreva um programa que receba um número 
inteiro x e avalie a função polinomial
p(x) = 3x³ - 5x² + 2x - 1.
"""

x = float(input("Informe o valor de x: "))

f_De_X = (3 * x * x * x) - (5 * x * x) + (2 * x - 1)

print(f_De_X)
