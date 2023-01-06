"""
Ranges

Precisa conhecer o loop for para utilizar o range, sendo utilizado para gerar sequencias numericas de maneira especifica não de maneira aleatoria.

Formas gerais:

range(valor_de_parada)
valor_de_parada não inclusive (inicio em 0, e passo de 1 em 1)
"""

# Forma 1
for num in range(11):
    print(num)

# Forma 2
for num in range(4, 11):
    print(num)

# Forma 3
for num in range(1, 10, 2):
    print(num)

# Forma 4
for num in range(10, -1, -1):
    print(num)