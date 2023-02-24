lista = []
for x in range(6):
    for y in range (3):
        lista.append((x,y))
print(lista)

lista = [(x,y) for x in range(6) for y in range(3)]
print(lista)

produto = {
    'nome': 'caneta azul',
    'preco': 2.5,
    'categoria': 'Escritório'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'categoria' # aqui ele remove Filter
}
print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c')
]

dc = {
    chave: valor
    for chave, valor in lista
}
print(dc) #ou poderia fazer print(dict(lista)) é a mesma coisa