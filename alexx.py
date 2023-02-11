valor = int(input(f'Informe um número: '))

while valor >= 1:
    cont = 0
    cont2 = 2
    while True:
        if cont2 >= valor:
            break
        if valor % cont2 != 0:
            cont2 += 1
            cont += 1
        else:
            ...
            break
    if cont == (valor - 2):
        print(f'{valor} É primo! ')
    valor -= 1
    