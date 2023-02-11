def juros (c, i, t):
    i = i / 100
    mont = ((1 + i) ** t) * c
    return f'{mont:.2f}'

cap = float(input(f'Informe seu Capital inicial: '))
taxa = int(input(f'Informe a taxa de juros em porcentagem: '))
tempo = int(input(f'Informe quantos meses: '))
print(juros(cap, taxa, tempo))