n = int(input())
x = 0

soma_par = 0
soma_impar = 0

while x < n:
    s = int(input())

    if s % 2 == 0:
        soma_par = soma_par + s
    else:
        soma_impar = soma_impar + s
    
    x = x + 1

print("A soma dos números pares da sequência é " + str(soma_par))
print("A soma dos números ímpares da sequência é " + str(soma_impar))
