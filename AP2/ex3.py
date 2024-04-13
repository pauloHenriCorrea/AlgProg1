"""
Leia o tempo de início e o tempo de fim de um jogo, em horas e minutos (hora inicial, hora final, minuto inicial, minuto final).
Logo após, imprima a duração do jog no seguinte formato: "O jogo durou X hora(s) e Y minuto(s)"

Obeservações:
- O jogo pode começar em um dia e terminar no outro dia;
- A duração máxima de um jogo é de 24 horas, e a duração mínima de um jogo é de um minuto;
- As horas informadas seguem o formato contínuo. Ou seja, qualquer valor de hora informada está no
intervado entre 0 e 23
"""

hora_inicial = int(input("Informe a hora inicial: "))
hora_final = int(input("Informe a hora final: "))
minuto_inicial = int(input("Informe o minuto inicial: "))
minuto_final = int(input("Informe o minuto final: "))

