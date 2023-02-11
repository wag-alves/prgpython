
import datetime

da = input(f'Informe uma data DD/MM/AAAA: ')
lista = da.split('/')
da_2 = input(f'Informe a segunda data DD/MM/AAAA: ')
lista_2 = da_2.split('/')

data = datetime.date(int(lista[2]),int(lista[1]),int(lista[0]))
data_2 = datetime.date(int(lista_2[2]), int(lista_2[1]), int(lista_2[0]))
dif = data_2 - data

print(f'A diferença de dias entre as datas é de {dif.days} dias.')
