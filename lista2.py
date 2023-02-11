lista = []
for n in range(0,5):
    num = int(input(f'Informe um valor: '))
    lista.append(num)
print(lista)
x = sorted(lista)
print(f'O menor valor informado é {x[0]}.')
print(f'O maior valor informado é {x[-1]}.')
print(f'O menor valor encontra-se na {lista.index(x[0])+1}° posição.')
print(f'O maior valor encontra-se na {lista.index(x[-1])+1}° posição.')