valor_cliente = int(input())

# Computação
  # Cálculo pa
moduloPor100 = valor_cliente % 100
moduloPor50 = moduloPor100 % 50
moduloPor10 = moduloPor50 % 10
moduloPor5 = moduloPor10 % 5

  # Cálculo para saber qual o número de cédulas deve-se dar para o cliente
cedulas_de_100 = int(valor_cliente / 100) # Quantidades de cédulas de 100
cedulas_de_50 = int(moduloPor100 / 50) # Quantidades de cédulas de 50
cedulas_de_10 = int(moduloPor50 / 10) # Quantidades de cédulas de 10
cedulas_de_5 = int(moduloPor10 / 5) # Quantidades de cédulas de 5
cedulas_de_1 = moduloPor5 / 1 # Quantidades de cédulas de 1

concatenacao = (
  "A quantidade de cedulas necessárias é de: \n" +
  str(cedulas_de_100) + " cédulas de 100\n" +
  str(cedulas_de_50) + " cédulas de 50\n" +
  str(cedulas_de_10) + " cédulas de 10\n" +
  str(cedulas_de_5) + " cédulas de 5\n" +
  str(cedulas_de_1) + " cédulas de 1"
  )

# Saída de dados
print(concatenacao)