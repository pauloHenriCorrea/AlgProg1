N = int(input())

iguais = ""
encontrei = False
ultimoDigito = N % 10

N = N // 10

while N > 0 and encontrei == False:
    proximoDigito = N % 10

    if ultimoDigito == proximoDigito:
        iguais += str(ultimoDigito) + str(proximoDigito)
        encontrei = True
    ultimoDigito = proximoDigito
    N = N // 10

print("O número informado foi: " + str(N))
if encontrei:
    print("Sim")
else:
    print("Não")
