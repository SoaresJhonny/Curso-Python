#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

v = float(input('Qual é o preço do produto? R$'))

p = v * 5 / 100
d = v - p
d = round(d, 2)

r = (print('Com o desconto o produto sairá por apenas R${}'.format(d)))