def see():
    import pickle

    lista_geral = []
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
        lista_geral.append(lista)

    with open('datafile.txt','wb') as arquivo:
        pickle.dump(lista_geral, arquivo)
    return open('datafile.txt', 'rb').read()
print(see())
