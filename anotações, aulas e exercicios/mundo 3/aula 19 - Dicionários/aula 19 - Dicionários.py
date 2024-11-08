'''
--------------------------------------------------------------------
Para declarar um Dicionário: 

ex:
dados = dict()
ou
dados = {'nome': 'José', 'idade': '45', 'sexo': 'Masculino'}

-----------------------------

Para adicionar mais um elemento:

dados['estado'] = 'São Paulo'

-----------------------------

Para excluir um item:

del dados['sexo']

-----------------------------

Para alterar o valor de um item:

dados['nome'] = 'Pedro'

-----------------------------

Estrutura de um dicionário:

.values() - retorna todos os valores adicionados na lista. Ex: José, 45, Masculino, São Paulo

.keys() - retorna os nomes dos índices. Ex: nome, idade, sexo, estado

.items() - retorna keys e values. 
'''
'''
#Ex código:

pessoa = {'nome': 'Jhonny', 'idade': '18', 'sexo': 'masculino'}

print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos e é do sexo {pessoa["sexo"]}.')
print()
print(pessoa.keys())
print()
print(pessoa.values())
print()
print(pessoa.items())
'''

'''
#Dicionário dentro de uma lista:

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])
'''

'''
#Ex código um pouco mais complexo:

estado = {}
brasil = []

for c in range(1, 4):
    estado['uf'] = str(input(f'Digite o {c}º estado: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
    c += 1
    print()

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')
    print()
'''



'''
# exercicio 90 - Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

nome = str(input('Digite o nome do aluno: '))
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))

media = (nota1 + nota2) / 2

if media > 7.0:
    s = 'aprovado'
else:
    s = 'reprovado'

boletim = {}

boletim['Nome'] = nome
boletim['Média'] = media
boletim['Situação'] = s

print(f'O aluno {boletim["Nome"]} ficou com uma média de {boletim["Média"]}, portanto, está {boletim["Situação"]}.')
'''



'''
#exercício 91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}

ranking = {}

print('Valores sorteados: ')
print()

for k, v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(0.6)
    print()

print('Ranking dos jogadores:')
print()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    print()
    sleep(0.6)
'''



'''
#exercicio 92 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (Homens 35 anos de contribuição para se aposentar, mulheres 30 anos).

from datetime import datetime

dados = {}

dados['Nome'] = str(input('Nome: '))

dados['Sexo'] = str(input('Sexo [M/F]: '))[0].upper()
if dados['Sexo'] == 'M':
    dados['Sexo'] = 'Homem'
elif dados['Sexo'] == 'F':
    dados['Sexo'] = 'Mulher'

nasc = int(input('Ano de nascimento: '))

idade = datetime.now().year - nasc
dados['Idade'] = idade

dados['CTPS'] = int(input('Carteira de Trabalho (Digite 0 caso não tenha): '))
if dados['CTPS'] != 0:
    contratacao = int(input('Ano de contratação: '))
    dados['Ano de contratação'] = contratacao
    dados['Salário'] = float(input('Salário: R$'))

print()

for k, v in dados.items():
    print(f'{k}: {v}')

if dados['Sexo'] == 'Homem':
    anos_trabalhados = datetime.now().year - contratacao
    if anos_trabalhados > 35:
        print(f'{dados["Nome"]} já trabalhou {anos_trabalhados} anos, portanto, já pode se aposentar.')
    else:
        falta_trabalhar = 35 - anos_trabalhados
        aposentadoria = idade + falta_trabalhar
        dados['Aposentadoria'] = aposentadoria
        print(f'{dados["Nome"]} irá se aposentar aos {aposentadoria} anos.')

if dados['Sexo'] == 'Mulher':
    anos_trabalhados = datetime.now().year - contratacao
    if anos_trabalhados > 30:
        print(f'{dados["Nome"]} já trabalhou {anos_trabalhados} anos, portanto, já pode se aposentar.')
    else:
        falta_trabalhar = 30 - anos_trabalhados
        aposentadoria = idade + falta_trabalhar
        dados['Aposentadoria'] = aposentadoria
        print(f'{dados["Nome"]} irá se aposentar aos {aposentadoria} anos.')

print()
print()
print()
print(dados)
'''



'''
#exercicio 93 -  Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

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
'''


'''
#exercicio 94 - Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

dados = {}
lista = []
pessoas = 0
somaidade = 0
mulheres = []

while True:
    nome = str(input('Nome: ')).title()

    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        print()
        print('\033[0;31;40mOpção inválido. Tente novamente.\033[m')
        sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]

    #adiciona o nome da pessoa a lista "mulheres"
    if sexo == 'F':
        mulheres.append(nome)

    idade = int(input('Idade: '))
    somaidade += idade #vai acrescentando e somando as idades das pessoas, para que o valor final possa ser usado na média de idades
    
    pessoas += 1 #conta o número de pessoas cadastradas para cumprir um dos requisitos do exercicio
    print()

    #adiciona os dados das pessoas ao dicionário
    dados['Nome'] = nome
    dados['Sexo'] = sexo
    dados['idade'] = idade

    lista.append(dados.copy())
    
    continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: '))[0].upper()
    while continuar not in 'SN':
        print('\033[0;31;40mOpção inválida. Tente novamente.\033[m')
        print()
        continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: '))[0].upper().strip()
        print()
    if continuar == 'N':
        break
    print()


print()
print(f'Foram cadastradas {pessoas} pessoas. ')
print()
mediaidades = somaidade / pessoas
print(f'A média de idade é de {mediaidades:.2f} anos.')
print()

if mulheres:
    print(f'As mulheres cadastradas foram: {", ".join(mulheres)}.')
else:
    print('Nenhuma mulher foi cadastrada.')
print()

pessoas_acima_media = []
for pessoa in lista:
    if pessoa['idade'] > mediaidades:
        pessoas_acima_media.append(pessoa)

print('Pessoas com idade acima da média:')
for pessoa in pessoas_acima_media:
    print(f'Nome: {pessoa["Nome"]}, Sexo: {pessoa["Sexo"]}, Idade: {pessoa["idade"]}')
'''



#exercicio 95 - Não feito
