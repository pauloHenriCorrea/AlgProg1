etrd = input().split()

cod = int(etrd[0])
qtd = int(etrd[1])

if cod == 1:
    total = qtd * 4
    print("Total: R$ " + str("%.2f" % total))

elif cod == 2:
    total = qtd * 4.5
    print("Total: R$ " + str("%.2f" % total))

elif cod == 3:
    total = qtd * 5
    print("Total: R$ " + str("%.2f" % total))

elif cod == 4:
    total = qtd * 2
    print("Total: R$ " + str("%.2f" % total))

else:
    total = qtd * 1.50
    print("Total: R$ " + str("%.2f" % total))
