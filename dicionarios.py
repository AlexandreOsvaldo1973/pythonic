dados = {
    'nome': 'Sao Paulo',
    'temperatura': '18 graus',
    'area km2': '1200',
    'populacao': 12.18,
}

print(type(dados))
print(dados)

dados['pais'] = 'Brasil'
print(dados)
print(dados['nome'])

dados['area km2'] = 1500
print(dados)

dados_2 = dados
dados_2['nome']= 'Curitiba'
print(dados_2)

dados_3 = dados.copy()
