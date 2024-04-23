senha = "2002"
x = input()
l = []

if x == senha:
    l.append("Acesso Permitido")
else:
    l.append("Senha Invalida")
while x != senha:
    x = input()
    if x == senha:
        l.append("Acesso Permitido")
    else:
        l.append("Senha Invalida")


for i in range(len(l)):
    print(l[i])
