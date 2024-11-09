#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar (Homens 35 anos de contribuição para se aposentar, mulheres 30 anos).

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