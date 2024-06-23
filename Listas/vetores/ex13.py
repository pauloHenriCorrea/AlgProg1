def verifica_se_a_existe_em_b(A, B):
    i = 0
    l = []
    while i < len(B):
        j = 0
        existe = False
        while j < len(A):
            if B[i] == A[j]:
                existe = True
            j += 1
        i += 1
        l.append(existe)
    return l


def sub_conjunto(v):
    i = 0
    while i < len(v):
        if not v[i]:
            return False
        i += 1
    return True


A = input().split()
B = input().split()

menor = A
maior = B

if len(A) < len(B):
    menor = B
    maior = A

result = sub_conjunto(verifica_se_a_existe_em_b(menor, maior))
print(result)
