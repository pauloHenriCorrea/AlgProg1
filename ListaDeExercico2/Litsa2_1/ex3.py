"""
Escreva um algoritmo que lê quatro valores inteiros e os imprime em
ordem decrescente.
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

# 
if a < b:
  aux = a
  a = b
  b = aux

# 
if a < c:
  aux = a 
  a = c
  c = b
  b = aux
elif b < c:
  aux = b
  b = c
  c = aux

# 
if a < d:
  aux = a
  a = d
  d = c
  c = b
  b = aux
elif b < d:
  aux = b
  b = d
  d = c
  c = aux
elif c < d:
  aux = c
  c = d
  d = aux