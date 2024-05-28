'''
# modos de manipular texto:

ex:
nomedavariavel = print('Cachorros gostam muito de comer ração')


------FATIAMENTO------

nomedavariavel[5] - pega o caracter de número 5 = r

nomedavariavel[5:10] - pega os caracteres do número 5 ao 10 = rros g

nomedavariavel[5:10:2] - pega os caracteres do número 5 ao 10 pulando de 2 em 2 = ro g

nomedavariavel[:10] - pega os caracteres do 0 ao 10 = Cachorros g

nomedavariavel[10:] - pega os caracteres do 10 até o último = gostam muito de comer ração

len(nomedavariavel) - conta a quantidade de caracteres (inclusive espaços) = 36

nomedavariavel.count('a') - conta a quantidade de caracteres 'a' dentro da string (diferencia maíusculos de minúsculos) = 3

nomedavariavel.count('a', 0, 13) - conta a quantidade de caracteres 'a' do ínicio da string ao caracter 13 = 1

nomedavariavel.find('ção') - conta quantas vezes foi encontrado o grupo de caracteres 'ção' dentro da string (caso não seja encontrado, irá retornar -1) = 1

'gostam' in nomedavarialvel - analisa se existe o grupo de caracteres na string, caso tenha, retorna true, caso contrário, false = true




------TRANSFORMAÇÃO------

nomedavariavel.replace('Cachorros', Gatos') - Troca a primeira palavra pela segunda palavra = Gatos gostam muito de comer ração

nomedavariavel.upper() - transforma todas as letras em maiúsculo = CACHORROS GOSTAM MUITO DE COMER RAÇÃO

nomedavariavel.lower() - transforma todas as letras em minúsculo = cachorros gostam muito de comer ração

nomedavariavel.capitalize() - transforma apenas a primeira letra da string para maiúsculo = Cachorros gostam muito de comer ração

nomedavariavel.title() - Transforma a primeira letra de cada palavra em maiúsculo = Cachorros Gostam Muito De Comer Ração 

nomedavariavel.strip() - remove os espaços antes e depois das letras da string
ex:
antes - '   Cachorros gostam muito de comer ração  '
depois - 'Cachorros gostam muito de comer ração'

nomedavariavel.lstrip() - remove os espaços da esquerda da string

nomedavariavel.rstrip() - remove os espaços da direita da string





------DIVISÃO------

nomedavariavel.split() - faz uma divisão no local de cada espaço da string, após cada espaço a contagem de cada caracter é resetada, e cada palavra separada é colocada em uma lista numerada
ex:

antes do split - 'que beleza'
                  0123456789

depois do split - '|que| |beleza|'
                    012   012345
                   | 1 | |   2  |  (numero de cada item da lista, que: item 1
                                                                  beleza: item 2)

'-'.join(nomedavariavel) - junta todos os itens pelo caracter colocado entre aspas simples = que-beleza
'''




'''
# exercicio 22 - Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maíusculas e minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
print('Seu nome é {}.'.format(nome.title()))
print('Seu nome em maiúsculo é {}.'.format(nome.upper()))
print('Seu nome em minúsculo é {}.'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))


# exercicio 23 - Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10 
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10


print('Analisando o número {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('centena: {}'.format(c))
print('Milhar: {}'.format(m))


# exercicio 24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Escreva o nome da cidade em que você nasceu: ')).strip()

cidade = cidade.lower()
print(cidade[:5] == 'santo')



# exercicio 25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Escreva seu nome completo: '))
print('silva' in nome.lower())


# exercicio 26 - Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra "A", em que posição ela aparece pela primeira vez e em que posição ela aparece pela última vez.

frase = str(input('Escreva uma frase qualquer: ')).lower().strip()

print('A letra "a" aparece {} vezes nessa frase.'.format(frase.count('a')))

print('A primeira letra "a" aparece na posição {} dessa frase.'.format(frase.find('a')+1))

print('A ultima letra "a" aparece na posição {} dessa frase.'.format(frase.rfind('a')+1))


# exerciio 27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip().title()
nome = n.split()

print('Olá, é um prazer te conhecer. Seu primeiro nome é {} e o último é {}.'.format(nome[0], nome[len(nome)-1]))
'''