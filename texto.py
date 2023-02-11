lista_geral = []
arquivo = open('pessoas.txt','w')
while True:
    lista = []
    nome = input(f'Informe seu nome:')
    if nome == 'END':
        break
    nome_final = nome.replace(' ', ',')
    lista.append(nome_final)
    email = input(f'Infrome o seu email: ')
    if email == 'END':
        break
    lista.append(email)
    arquivo.write('Nome:')
    arquivo.write(nome_final)
    arquivo.write('; ')
    arquivo.write('Email:')
    arquivo.write(email)
    arquivo.write(' \n')
    lista_geral.append(lista)
arquivo.close()