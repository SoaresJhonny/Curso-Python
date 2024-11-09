#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

r = float(input('Digite quantos reais você tem no banco: '))

tdc = 4.99

d = r / tdc 
d = round(d, 2)

print('Com esse dinheiro você consegue comprar {}'.format(d))