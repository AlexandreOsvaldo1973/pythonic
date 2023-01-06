"""
Loop -> estrutura de repetição
For -> Estrutura de repetição

for item in interavel:
    // execução do loop

Utiliza loop para iterar sequencias ou valores iteraveis:
    - string
    - lista
    - range
"""
nome = 'Monalisa'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)

# Exemplo for 1
for letra in nome:
    print(letra)

# Exemplo for 2
for numero in lista:
    print(numero)

# Exemplo for 3
for numero in range(1, 10):
    print(numero)

for i, v in enumerate(nome):
    print(nome[i])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Qual é o range? '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
    print(f'A soma é  {soma}')

for letra in nome:
    print(letra, end='')

emoji = 'U0001F60D'

for num in range(1, 12):
    print(f'\U0001F60D' * num)
