#Algoritmo para aprender listas
# 13/09/2022

nomes_paises = ['Brasil','Argentina','China','Canadá']
print(nomes_paises)
print('Tamanho da lista', len(nomes_paises))
print('Pais: ', nomes_paises[3])
print('Pais: ', nomes_paises[-1])
nomes_paises[3] = 'Colombia'
print('Pais: ', nomes_paises[3])
print(nomes_paises)
print(nomes_paises[1:3])
print(nomes_paises[1:-1])
print(nomes_paises[2:])
print(nomes_paises[:3])
print(nomes_paises[:])
print(nomes_paises[::2])
print(nomes_paises[::-1])
print("Brasil" in nomes_paises)
print("Canadá" not in nomes_paises)

listas_capitais = []
listas_capitais.append('Brasilia')
listas_capitais.append('Buenos Aires')
listas_capitais.append('Pequim')
listas_capitais.append('Bogotá')
print(listas_capitais)
listas_capitais.insert(2, 'Paris')
listas_capitais.remove('Buenos Aires')
removido = listas_capitais.pop(2)
print(listas_capitais, removido)