"""
Saindo de loop com break
Funciona como em C o Java

Utilizado para sair de um loop de maneira forcada ou projetada

"""
# Exemplo 01

for num in range(1, 11):
    if num == 6:
        break
    else:
        print(num)
print('Sai do loop')

# Exemplo 2

while True:
    comand = input('Digite sair para terminar: ')
    if comand == 'sair':
        break