
valor = int(input(f'Digite o valor que deseja sacar: '))


def caixa (value):
    total = value
    a = b = c = d = e = 0
    din = 50
    while True:
        if total == 0:
            break
        if total >= din:
            total -= din
            if din == 50:
                a += 1
            if din == 20:
                b += 1
            if din == 10:
                c += 1
            if din == 5:
                d += 1
            if din == 1:
                e += 1
        else:
            if din == 50:
                din = 20
            elif din == 20:
                din = 10
            elif din == 10:
                din = 5
            elif din == 5:
                din = 1
    return {'50' : a, '20' : b, '10' : c, '5' : d, '1' : e}

print(caixa(valor))