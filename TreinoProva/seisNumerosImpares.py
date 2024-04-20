x = float(input())
for n in range(6):
    if x % 2 == 0:
        x += 1
    print("%.0f" % x)
    x += 2
