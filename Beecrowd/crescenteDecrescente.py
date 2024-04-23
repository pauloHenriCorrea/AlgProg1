l = []
x = input().split()
x0 = int(x[0])
x1 = int(x[1])

if x0 > x1:
    l.append("Decrescente")
else:
    l.append("Crescente")

while x0 != x1:
    x = input().split()
    x0 = int(x[0])
    x1 = int(x[1])

    if x0 > x1:
        l.append("Decrescente")
    elif x0 < x1:
        l.append("Crescente")

for i in range(len(l)):
    print(l[i])
