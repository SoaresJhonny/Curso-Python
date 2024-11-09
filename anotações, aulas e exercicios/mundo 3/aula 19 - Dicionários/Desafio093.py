#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

dados = {}
dados['Nome'] = str(input('Digite o nome do jogador: ')).title()
partidas = int(input(f'Digite o número de partidas jogadas por {dados["Nome"]}: '))
gols = []
dados['Gols'] = gols
print()

for g in range(partidas):
    gol = int(input(f'Digite a quantidade de gols que {dados["Nome"]} fez na {g+1}º partida: '))
    gols.append(gol)
    g += 1

dados['Total de gols'] = sum(gols)

print()
print(dados)
print()

for k, v in dados.items():
    print(f'O campo "{k}" tem valor "{v}".')

print()
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas.')
print()

for p in range(len(gols)):
    print(f'=> Na {p+1}ª partida, fez {gols[p]}.')

print(f'Foi um total de {dados["Total de gols"]} gols.')
print()