# Algoritmos com tuplas
# 13/09/2022

nomes_paises = ('Brasil','Japão','Inglaterra','Rússia')
print(nomes_paises, type(nomes_paises))
print(len(nomes_paises))
print(nomes_paises[0])
b, j, i, r = nomes_paises
print(b, i, j)

frase = "Datr Vader disse: \"Eu sou o seu pai\""
print(frase)

empresa = 'Google'
print(empresa[0])
print(empresa[:3])

nome_cidades = "'São Paulo', 'Rio de Janeiro', 'Brasilia','Curitiba'"
nome_cidades = nome_cidades.split(', ')
print(nome_cidades)

cabecalho = "      MENU PRINCIPAL       "
print(cabecalho.strip())

cidade = 'Rio de Janeiro'

print(cidade.title())
print(cidade.capitalize())
print(cidade.lower())
print(cidade.upper())

nome_cidade = input('Qual o nome da cidade maravilhosa? ')
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() !='rio de janeiro':
    print('Tente de novo.')
    nome_cidade = input('Não é essa cidade...')
print('Essa mesmo!')

nome = 'Monalisa'
idade = 2
patas = 4
print('{} tem {} anos e {} patas.'.format(nome, idade, patas))
print(f'{nome} tem {idade} anos e {patas} patas.')

preco_gas = 103.567
print('O preço do gás é R$ {:.2f}'.format(preco_gas))

