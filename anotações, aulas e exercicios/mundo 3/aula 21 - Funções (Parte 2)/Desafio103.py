#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome=0, gols=0):
    if not nome:
        nome = "<desconhecido>"
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if s == 'F':
        return f'A jogadora {nome} fez {gols} gols.'
    else:
        return f'O jogador {nome} fez {gols} gols'

#programa principal:
nome = str(input('Digite o nome do jogador: ')).title().strip()

while True:
    s = str(input('Digite o sexo [M/F]: ')).capitalize().strip()
    if s == 'F':
        gols = str(input(f'Digite quantos gols a jogadora {nome} fez: '))
        break
    elif s == 'M':
        gols = str(input(f'Digite quantos gols o jogador {nome} fez: '))
        break
    else:
        print('opção inválida. Tente novamente digitando apenas "M" ou "f".')

print(ficha(nome, gols))