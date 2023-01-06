'''
LISTAS

Listas são como vetores/matrizes (arrays), sendo dinâmicas e aceitam qualquer tipo de dados.

- Dinâmico: não possui tamanho fixo, aceita qualquer quantidade de elementos;
- Qualquer tipo de dados, não possue tipo de dados fixo;
- São representadas por colchetes [ ]

'''

lista1 = [1,3,5,7,9,2,4,6,8,10,11]
lista2 = ['A','l','e','x','a','n','d','r','e']
lista3 = []
lista4 = list(range(11))
lista5 = list('Alexandre Osvaldo')

# Checar se um valor está contido na lista

num = 7
if num in lista4:
    print(f'Valor encontrado')
else:
    print(f'Valor inexistente')

if 'u' in lista5:
    print('A letra "u" existe')
else:
    print('A letra "u" não existe') # parou em 20:37 minutos