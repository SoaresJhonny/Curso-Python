#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

#A média de idade do grupo.
#Qual é o nome do homem mais velho
#Quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
idadef = 0
totalmulheres = 0

print('Digite as informações das pessoas:')
print()

for p in range (0, 5):
    # recebe os dados das pessoas
    print('-----{}ª PESSOA-----'.format(p+1))
    print()
    nome = str(input(f'Nome: ')).title()
    idade = int(input(f'Idade: '))
    s = str(input(f'Sexo [M/F]: ')).lower()
    print()
    somaidade += idade   #soma a idade de todos para fazer a média no final
   
    if s == 'm':
        if idade > maioridadehomem:  # se a pessoa for do sexo masculino e tiver a idade maior do que a maior idade já registrada na variável "maioridadehomem", então passará a ser o homem mais velho
            maioridadehomem = idade
            nomevelho = nome
    elif s == 'f':
        totalmulheres += 1  # conta o total de mulheres
        if idade < 20:  # se o sexo for feminino e a idade for menor que 20, então acrescentará mais uma mulher na contagem de mulheres com menos de 20 anos de idade
            idadef += 1  # acrescenta mais um no total de mulheres com a idade abaixo de 20 anos

print()
media = somaidade / 5   #média da idade
print('A média da idade do grupo é de {:.1f}.'.format(media))


if maioridadehomem > 0: #Verifica se existe algum homem no grupo, pois caso não tenha, essa mensagem não será exibida
    print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
else:
    print('Não há nenhum homem neste grupo.')


if totalmulheres > 0: #Verifica se existe alguma mulher no grupo, pois caso não tenha, essa mensagem não será exibida
    if idadef == 1:
        print('Ao todo, apenas uma mulher tem a idade abaixo de 20 anos.')
    elif idadef == 0:
        print('Nenhuma mulher tem menos de 20 anos.')
    else:
        print('Ao todo, {} mulheres tem a idade abaixo de 20 anos.'.format(idadef))
else:
    print('Não há nenhuma mulher neste grupo.')