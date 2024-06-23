"""
Leia o tempo de início e o tempo de fim de um jogo, em horas e minutos (hora inicial, hora final, minuto inicial, minuto final).
Logo após, imprima a duração do jog no seguinte formato: "O jogo durou X hora(s) e Y minuto(s)"

Obeservações:
- O jogo pode começar em um dia e terminar no outro dia;
- A duração máxima de um jogo é de 24 horas, e a duração mínima de um jogo é de um minuto;
- As horas informadas seguem o formato contínuo. Ou seja, qualquer valor de hora informada está no
intervado entre 0 e 23
"""

tempo_inicial = input("Informe a hora inicial em hh:mm do jogo: ")
tempo_final = input("Informe a hora final em hh:mm do jogo: ")


def split(strs, sep=None):
    l = []
    cursor = ""

    for char in strs:
        if char == sep:
            l.append(int(cursor))
            cursor = ""
            continue
        cursor += char

    l.append(int(cursor))
    return l


tempo_inicial = split(tempo_inicial, ":")
tempo_final = split(tempo_final, ":")

hi = tempo_inicial[0]  # * Hora inicial = hi
mi = tempo_inicial[1]  # * Minuto inicial = mi

hf = tempo_final[0]  # * Hora final = hf
mf = tempo_final[1]  # * Minuto final = mf

# * Caso 1: começar e terminar no mesmo dia e mf > mi
if hf > hi and mf > mi:
    h = hf - hi  # * Horas = h
    m = mf - mi  # * Minutos = m

# * Caso 2: começar e terminar no mesmo dia e o minuto final for menor que e o minuto inicial
elif hf > hi and mf < mi:
    h = (hf - hi) - 1  # * Horas = h
    m = (60 - mi) + mf  # * Minutos = m

# * Caso 3: começar em um dia e terminar no outro e o mf > mi
elif hf < hi and mf > mi:
    # * horas = diferança de hf - hi (que vai dar um número negativo), somado com 24, que é um dia inteiro
    h = (hf - hi) + 24
    m = mf - mi  # * Minutos = m

# * Caso 4: começar em um dia e terminar no outro e mf < mi
elif hf < hi and mf < mi:
    h = (hf - hi) + 23
    m = (mf - mi) + 60

# * Formatando a saída para o usuário
if h < 10:
    h = "0" + str(h)
if m < 10:
    m = "0" + str(m)

print("O jogo durou por " + str(h) + " hora(s) e " + str(m) + " minuto(s)")
