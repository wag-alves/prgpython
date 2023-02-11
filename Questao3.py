def area (b, h):
    ar = b * h
    per = b + b + h + h
    val = (ar, per)
    return f'A Área é de {val[0]}m², e tem o perímetro de {val[1]}m'

x = float(input(f'Qual o comprimento? '))
y = float(input(f'Qual a largura? '))
print(area(x, y))
    