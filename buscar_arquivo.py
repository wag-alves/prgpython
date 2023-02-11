import os 

def buscar(caminho, arquivo):
    info = []
    for path, _, files in os.walk(caminho):
        try:
            for x in files:
                if arquivo in x:
                    info.append(os.path.abspath(os.path.join(path, arquivo)))
        except ValueError:
            return 'Erro'
    return info


local = input(f'Onde? ')
o_que = input(f'O quê? ')

print(buscar(local, o_que))