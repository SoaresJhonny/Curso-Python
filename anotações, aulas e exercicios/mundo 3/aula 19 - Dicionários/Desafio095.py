#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
from time import sleep

todos = []
resumo = {}
total = 0
print('=' * 40)
print(f'{"ESTATÍSTICAS DAS PARTIDAS":^40}')
while True:
    gols = []
    print('=' * 40)
    resumo['nome'] = str(input('Nome do jogador: ')).strip().title()
    resumo['partidas'] = int(input('Partidas jogadas: '))
    print('-' * 40)
    for p in range(0, resumo['partidas']):
        gols.append(int(input(f'Gols marcados na {p + 1}º partida: ')))
        total += gols[p]
    resumo['gols'] = gols.copy()
    resumo['total'] = total
    todos.append(resumo.copy())
    resumo.clear()
    gols.clear()
    total = 0
    print('-' * 40)
    print()
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    print()
    while continuar not in 'SN':
        print()
        print('Opção inválida. Use S para SIM e N para NÃO.')
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        print()
    if continuar == 'N':
        break
sleep(1)

while True:
    print('=' * 40)
    print(f'{"ESTATÍSTICAS INDIVIDUAIS":^40}')
    print('=' * 40)
    print(f'{"N°":<5}' + f'{"NOME":<14}' + f'{"PARTIDAS":<14}' + f'{"GF"}')
    print('-' * 40)
    for c in range(0, len(todos)):
        print(f'{c + 1:<5}' + f'{todos[c]["nome"]:<14}' + f'{todos[c]["partidas"]:<14}' + f'{todos[c]["total"]}')
    print('=' * 40)
    print()
    detalhes = str(input('Deseja ver detalhes dos jogadores? [S/N] ')).strip().upper()[0]
    while detalhes not in 'SN':
        print()
        print('Opção inválida. Use S para SIM e N para NÃO.')
        detalhes = str(input('Deseja ver detalhes dos jogadores? [S/N] ')).strip().upper()[0]
    if detalhes == 'N':
        break
    print('-' * 40)
    selecione = int(input('Nº do jogador para detalhes: '))
    while selecione not in range(1, len(todos) + 1):
        print()
        print('opção inválida. Selecione um Nº correspondente a um jogador da lista.')
        selecione = int(input('Nº do jogador para detalhes: '))
    print('-' * 40)
    sleep(0.5)
    print(f'Jogador selecionado: {todos[selecione - 1]["nome"]}')
    sleep(0.5)
    for c in range(0, todos[selecione - 1]['partidas']):
        print(f'Gols no {c + 1}º jogo: {todos[selecione - 1]["gols"][c]}')
        sleep(0.5)
    sleep(5)
    print('-' * 40)
sleep(0.5)
print()
print('=' * 40)
print(f'{"PROGRAMA FINALIZADO":^40}')
print('=' * 40)