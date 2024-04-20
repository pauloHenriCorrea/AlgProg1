n = int(input())
q = 0

for x in range(int(n / 2)):
    q += 2
    x = q**2
    print(str(q) + "^2 = " + str(x))
