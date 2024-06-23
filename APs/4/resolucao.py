# Atividade prática 4

# 1 - O programa dirá sim se no número digitado conter 2 ou mais digitos em sequência um do outro, e não caso não tenha.
# Por exemplo: ele irá aceitar 133, pois a dois digitos "3" em sequência, porém não irá aceitar 313, pois, mesmo que o digito "3" apareça duas vezes, não está em sequência

# Linha             # valor     # existe    # anterior      #atual      #comeco
# 1                 133         -           -               -           -
# 2                 133         False       -               -           -
# 3                 133         False       0               -           -
# 4                 133         False       0               0           -
# 5                 133         False       0               0           True
# 6                 133         False       0               0           True
# 7                 133         False       0               0           True
# 8                 133         False       0               0           False
# 9                 133         False       3               0           False
# 10                13          False       3               0           False
# 11                13          False       3               0           False
# 12                13          False       3               0           False
# 13                13          False       3               0           False
# 14                13          False       3               3           False
# 15                13          False       3               0           False
# 16                13          True        3               0           False
# 17                1           True        3               0           False
# 18                1           True        3               0           False
# 19                1           True        3               0           False
# 20                1           True        3               0           False
# 21                1           True        3               0           False

# 2 - O programa irá escrever a sequência de Fibonacci até o valor do n-ésimo número da sequência (sendo n o valor digitado do teclado)

# Linha             # n     # penultimo    # ultimo      #mensagem      #i       #proximo
# 1                 4       -              -             -              -        -
# 2                 4       0              -             -              -        -
# 3                 4       0              1             -              -        -
# 4                 4       0              1             ""             -        -
# 5                 4       0              1             ""             -        -
# 6                 4       0              1             ""             -        -
# 7                 4       0              1             "0 1"          -        -
# 8                 4       0              1             "0 1"          2        -
# 9                 4       0              1             "0 1"          2        -
# 10                4       0              1             "0 1"          2        1
# 11                4       0              1             "0 1 1"        2        1
# 12                4       1              1             "0 1 1"        2        1
# 13                4       1              1             "0 1 1"        2        1
# 14                4       1              1             "0 1 1"        3        1
# 15                4       1              1             "0 1 1"        3        1
# 16                4       1              1             "0 1 1"        3        2
# 17                4       1              1             "0 1 1 2"      3        2
# 18                4       1              1             "0 1 1 2"      3        2
# 19                4       1              2             "0 1 1 2"      3        2
# 20                4       1              2             "0 1 1 2"      4        2
# 21                4       1              2             "0 1 1 2"      4        2
# 22                4       1              2             "0 1 1 2"      4        2
