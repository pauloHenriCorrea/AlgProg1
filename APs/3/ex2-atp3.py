a = 123.12312312312
print(round(a,2))

n = int(input())
x = 0

validador = True
ant = 0
while x < n:
    s = int(input())

    if s > ant:
        ant = s
    else:
        validador = False
    x = x + 1

if validador:
    print("É crescente")
else:
    print("Não é crescente")

a = 123.12312312312
print(round(a,2))