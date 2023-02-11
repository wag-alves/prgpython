campeonato = ( 'Atlético', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América', ' Atletico', 'Santos', 'Ceará', 'Internacional', 'São Paulo', ' Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
lista = []
for x in campeonato:
    lista.append(x)
print(f'Os 5 primeiros colocados do campeonato é {campeonato[:5]}')
print(f'Os 5 ultimos colocados do campeonato é {campeonato[-1:-6:-1]}')
lista.sort()
print(f'A Lista em ordem alfabética é {lista}')
print(f'Fortaleza encontra-se na {campeonato.index("Fortaleza")+1}° posição.')