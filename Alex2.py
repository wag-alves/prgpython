
arquivo_get = input(f'Informe o nome do arquivo: ')
lista =[]

with open(f'{arquivo_get}.txt','r') as arq:
    for valor in arq:
        lista.append(valor)

nova_l = ((str(lista)).lower()).replace('a','A')
novo_arq = input(f'Informe o nome do novo arquivo: ')
with open(f'{novo_arq}.txt','w+') as new_arq:
    new_arq.write(nova_l)