#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Camnpeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: 
# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# Uma lista com os times em ordem alfabética.
# em que posição na tabela está o time Fluminense

times = ('Athletico-PR', 'Bahia', 'Bragantino', 'Botafogo', 'Flamengo', 'São Paulo', 'Internacional', 'Cruzeiro', 'Atlético-MG', 'Palmeiras', 'Fortaleza', 'Grêmio', 'Vasco', 'Juventude', 'Corinthians', 'Fluminense', 'Criciúma', 'Atlético-GO', 'Vitória', 'Cuiabá')

print(f'Lista de times do Brasileirão: {times}')
print()
print(f'Os 5 primeiros times são: {times[0:5]}')
print()
print(f'Os 4 últimos times são: {times[-4:]}')
print()
print(f'Os times em ordem alfabética são: {sorted(times)}')
print()
print('O Fluminense está na posição {}.'.format(times.index('Fluminense')+1))