ss = int(input())

mm = 0
hh = 0

if ss > 60:
    mm += int(ss / 60)
    ss = ss % 60

if mm > 60:
    hh = int(mm / 60)
    mm = mm % 60
print(str(hh) + ":" + str(mm) + ":" + str(ss))
