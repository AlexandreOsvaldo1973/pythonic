"""
Listas funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem dinâmicos e também de podermos colocar qualquer tipo de dado.

Linguagem C ou Java: os arrays possuem tamanho e tipo de dados fixos;
Um array do tipo INT e com tamanho 5, este é imutável em tipo e tamanho;

Em python

- Dinâmico: não possue tamanho fixo; Ou seja pode criar a lista e adicionar elementos, conforme o tamanho da memória disponível;
- Qualquer tipo de dado: as listas não possuem tipo de dado fixo, podendo ser alterado para qualquer tipo de dado;

As listas são representadas por colchetes: [ ]

"""
type([])

lista1 = [1, 2, 3, 50, 120, 3]
lista2 = ['G', 'e', 'n', 'X']
lista3 = []
lista4 = list(range(11))
lista5 = list('Monalisa')

# Pode checar se deteerminado valor está contido na lista

num = 10

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')