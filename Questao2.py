def segundo(x):
    return x[1]


lista = []
while True:
    nome = input(f'Informe um nome, e peso caso deseje parar digite "pare": ')
    if nome == 'pare':
        break
    info = [item.strip() for item in nome.split(',')]
    lista.append(info)
new = sorted(lista, key=segundo)
print(lista)
print(new)
