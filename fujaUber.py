# O algoritmo descreve a situação de pegar um onibus ou pegar um uber
# 13/09/2022

valor_passagem = 5.40

valor_corrida = input('Qual o valor da corrida? ')

if float(valor_corrida) <= valor_passagem * 5:
    print('Pegue um uber')
elif float(valor_corrida) <= valor_passagem * 6:
    print('Aguarde que o valor pode abaixar!')
else:
    print('Pegue o onibus!')