"""
Loop While

Forma geral:

while expressao booleana
    // execucao do loop

O bloco while sera repetida enquanto a expressao booleana for verdadeira
Expressao booleana e toda expressao onde o resultado e verdadeiro ou falso

num = 5
num < 5 -- false
num < 6 -- true

"""

# Exemplo 01
num = 1

while num < 10:
    print(num)
    num = num + 1

# OBS: em um loop while eh importante cuidar com o criterio de parada *** loop infinito ***

# Exemplo 02

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou?')

