def primo(x):
    cont = 0
    prox = 2
    if x == 1:
        return False
    while True:
        if x == prox:
            break
        if x % prox == 0:
            cont += 1
        prox += 1
    if cont == 0:
        return True
    else:
        return False
valor = int(input(f'Informe um número: '))

print(primo(valor))

if primo == 'True':
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
else:
    print(f'O valor informado não é primo')
        