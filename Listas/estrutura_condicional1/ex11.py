# Entrada de dados
productPrice = float(input("Informe o preço do produto: "))

# Computação
# * Calcualndo o percentual de aumento do preço de um produto
if productPrice <= 50:
    # * Calculando o aumento de 5% no preço do produto
    ProductWith5percentIncrease = (
        productPrice * 0.05
    )  # * 0.05 equivale aos 5% de aumento no preço do produto
    newPrice = productPrice + ProductWith5percentIncrease
elif productPrice <= 100:
    # * Calculando o aumento de 10% no preço do produto
    ProductWith10percentIncrease = (
        productPrice * 0.10
    )  # * 0.10 equivale aos 10% de aumento no preço do produto
    newPrice = productPrice + ProductWith10percentIncrease
else:
    # * Calculando o aumento de 15% no preço do produto
    ProductWith15percentIncrease = (
        productPrice * 0.15
    )  # * 0.15 equivale aos 15% de aumento no preço do produto
    newPrice = productPrice + ProductWith15percentIncrease

# * Calculando a classificação do novo preço do produto, para saber se está barato, normal, caro ou muito caro e retornando para o usuário
if newPrice <= 80:
    print("Barato!")
elif newPrice <= 120:
    print("Normal!")
elif newPrice <= 200:
    print("Caro!")
else:
    print("Muito caro!")
