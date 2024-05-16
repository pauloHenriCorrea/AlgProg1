N = int(input())

i = 0
par = 0
impar = 0

while i < N:
    passo = True
    while passo != False:
        x = int(input())

        if x == 0:
            passo = False

        if x % 2 == 0:
            par += x
        else:
            impar += x
    i += 1
    print(par, impar)
