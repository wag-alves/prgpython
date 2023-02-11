par = []
lista = []
impar = []
while True:
    num = int(input(f'Informe valores, caso deseje parar digite 0: '))
    if num == 0:
        break
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(f'Os valores {par} são pares!')
print(f'Os valores {impar} são ímpares!')
print(f'Todos os números digitados foram: {lista}')