# Lista
# Lista de inteiros
lista1 = [2, 31, 1, "ss"]

lista2 = ["Jose", "Maria"]

lista3 = ['oi', 3.0, 40, True]

print(lista2)
lista2.insert(0, 'Pedro')
print(lista2)
lista2.append('Paulo')
print(lista2)

# Dicionários
contatos = {
    'Pedro': '9997-5678',
    'Carlos': '9999-9999',
    'Beatriz': '8768-4321',
    'Marina': '8888-7575',
    'Eduardo': '8797-4567'
}
print(contatos.keys())  # Chaves: Pedro Carlos...
print(contatos.values())  # Valores: 8797-4567
print(contatos.items())  # Itens, ou seja o dicionário
print(contatos.get('Beatriz')) # Consegue o valor com apartir da chave
contatos['Andre'] = '9988-1515'
print(contatos)
print(" ")
for key, value in contatos.items():
    print(f'Nome: {key} - Telefone: {value}')
