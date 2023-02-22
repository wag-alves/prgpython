lista = []
for x in range(6):
    for y in range (3):
        lista.append((x,y))
print(lista)

lista = [(x,y) for x in range(6) for y in range(3)]
print(lista)