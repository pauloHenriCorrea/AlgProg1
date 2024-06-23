"""
Para transformar um número inteiro i no menor inteiro m maior que i e múltiplo
de um número inteiro j, a seguinte fórmula pode ser utilizada:

m = i + j - i mod j ,

onde o operador mod é o operador de resto de divisão inteira na notação matemática
usual, que corresponde ao nosso operador %.

Por exemplo, suponha que usamos i = 256 dias para alguma atividade e queremos saber 
qual o total de dias m que devemos ter de forma que esse número seja divisível por j = 7, 
para termos uma ideia do número de semanas que usaremos na atividade. 
Então, pela fórmula acima, temos que

m = 256 + 7 - 256 mod 7
m = 256 + 7 - 4
m = 259 

Escreva um programa que receba dois números inteiros positivos i e j e devolva
o menor inteiro m maior que i e múltiplo de j. Faça a simulação passo a passo
da execução de sua solução.
"""
# Entrada de dados
i = int(input("Informe um número inteiro: "))
j = int(input("Informe outro número inteiro: "))

# Computação
m = (i + j) - (i % j)

# Saída
print(m)
