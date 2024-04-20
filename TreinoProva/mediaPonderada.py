N = int(input())

for i in range(N):
    x = input().split()
    media = (float(x[0]) * 2 + float(x[1]) * 3 + float(x[2]) * 5) / 10

    print("%.1f" % media)
