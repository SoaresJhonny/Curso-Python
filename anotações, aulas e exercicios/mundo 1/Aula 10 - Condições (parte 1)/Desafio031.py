#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200Km e R$ 0,45 para viagens mais longas.

d = int(input('Digite quantos Km tem essa viagem: '))

if d <= 200:
    preco = d * 0.50
else:
    preco = d * 0.45
print('O preço da passagem será de R${:,.2f}'.format(preco).replace('.', ','))