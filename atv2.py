x = []
while True:
    num = input(f'Informe um valor, caso deseje parar digite FIM: ')
    if num == 'FIM':
        break
    print(num)
    x.append(int(num))
    y = [m * 3 for m in x]
print(x)
print(y)