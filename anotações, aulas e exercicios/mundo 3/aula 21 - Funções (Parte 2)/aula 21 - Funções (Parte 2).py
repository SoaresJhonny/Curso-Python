'''
#exercicio 101 - Crie um programa que tenha uma função chamda voto() que vai receber como parâmetro o ano de nascimetno de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from time import sleep 

print('Verificação de Voto\nPara descobrir se pode votar, respondar as perguntas abaixo:')
sleep(1.6)
print()

def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    
    if idade < 16:
        return f'Com {idade} anos: Não pode votar!'

    while True:
        alf = str(input('É alfabetizado(Sabe ler e escrever)? [S/N]: ')).strip().upper()
        print()
        if alf in 'SN':
            break
        else: 
            print()
            print('Opção inválida! Digite S (Sim) ou N (Não).')
        print()


    if alf == 'S':
        if idade >= 16 and idade < 18:
            return f'Com {idade} anos: Voto Opcional!'
        elif idade >= 18 and idade < 70:
            return f'Com {idade} anos: Voto Obrigatório!'
        elif idade >= 70:
            return f'Com {idade} anos: Voto Opcional!'
        
    elif alf == 'N':
        if idade >= 16:
            return f'Com {idade} anos sendo analfabeto: Voto Opcional!'
        else:
            return f'Com {idade} anos: Não pode votar!'
    

#programa principal
ano_nascimento = int(input('Digite o ano de nascimento: '))
print(voto(ano_nascimento))
'''



# exercicio 102 - Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcula o fatorial do número digitado.
    :param num: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: Retorna o valor de n.
    """
    multiplicador = 1
    if show == True:
        for numero in range(num, 0, -1):
            print(numero, end='')
            if numero > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            multiplicador *= numero
        return multiplicador
    if show == False:
        multiplicador = 1
        print('-'*20)
        for numero in range(num, 0, -1):
            multiplicador *= numero
        return multiplicador


print(fatorial(5, True))



'''
#exercicio 103 - Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

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
'''


'''
#exercicio 104 - Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.


def leiaInt(txt):
    while True:
        if txt.isnumeric():
            print(f'Você acabou de digitar o número {txt}.')
            break
        else:
            txt = input(f'\033[0;31;40mERRO! Digite um número inteiro válido:\033[m ')
            continue
            
n = leiaInt(str(input('Digite um número inteiro: ')))
'''



'''
#exercicio 105 - Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

# Adicione também as docstrings da função.

def notas(*nts, sit=False):
    """
    -> Recebe quantidade de notas variáveis e calcula a quantidade total de notas, a maior nota, a menor nota, a média e a situação geral da turma.
    :param *nts: As notas que serão verificadas (Aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Print com várias informações sobre a situação da turma.
    """

    maior_nota = max(nts)
    menor_nota = min(nts)
    media = sum(nts) / len(nts)
    
    if media >= 8.0:
        situação = 'Boa'
    elif media < 8.0 and media >= 6.0:
        situação = 'Razoável'
    else:
        situação = 'Ruim'

    if sit == False:
        return f'Total: {len(nts)}  Maior: {maior_nota} Menor: {menor_nota}  Média: {media:.2f}'
    else:
        return f'Total: {len(nts)}  Maior: {maior_nota}  Menor: {menor_nota}  Média: {media:.2f}  Situação: {situação}'

#programa principal
resp = notas(5.0, 9.5, 7.0, 8.5, 6.5, 2.0, sit=True)
print(resp)
'''






