N = int(input())
i = 0
while i < N:
    a = input().split()

    x = int(a[0])
    y = int(a[1])

    if y == 0:
        print("divisao impossivel")
    else:
        div = x / y
        print(div)

    i += 1