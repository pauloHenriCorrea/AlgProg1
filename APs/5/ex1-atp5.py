def perfeito(perfect):
    count = 1
    soma = 0

    while perfect > count:
        if perfect % count == 0:
            soma = soma + count
        count = count + 1
    
    if soma == perfect:
        return True
    else:
        return False

perfect = int(input())
print("É perfeito? -> " + str(perfeito(perfect)))


