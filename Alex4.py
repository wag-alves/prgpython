x = []
cont = 0
while cont < 10:
    num = int(input(f'Informe um valor: '))
    cont = cont + 1
    if num in x:
        continue
    x.append(num)
x.sort()
print(x)
