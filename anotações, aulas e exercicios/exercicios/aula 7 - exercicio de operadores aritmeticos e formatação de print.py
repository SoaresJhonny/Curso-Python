'''
v1 = float(input('Digite um valor: '))
v2 = float(input('outro valor: '))
s = v1 + v2
m = v1 - v2
d = v1 / v2
di = v1 // v2
e = v1 ** v2

print('A soma é {},\no resultado da subtração é {},\na divisão é {}'.format(s, m, d), end=', ')
print('divisão interia é {} e a exponenciação é {}'.format(di, e))
'''



# exercicio 5 - mostrar o antecessor e o sucessor de um número digitado
'''
n = int(input('Digite um número para ver seu antecessor e seu sucessor: '))

a= n - 1

print('O antecessor de {} é: {}'.format(n, a))

s = n + 1

print('O sucessor de {} é: {}'.format(n, s))
'''


# exercicio 6 - criar um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada
'''
n = int(input('Digite um número: '))

d = n * 2
print('O dobro de', n, 'é: ', d)

t = n * 3
print('O triplo de', n, 'é: ', t)

rq = n * n
print('A raiz quadrada de', n, 'é: ', rq)
'''



# exercicio 7 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''
nome = input('Escreva o nome do aluno: ')

n1 = float(input('Digite a primeira nota: '))

n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2) / 2

print('A média do aluno(a) {} foi {}!'.format (nome, m))

if m >= 7:
      print('Aprovado')
else:
      print('Reprovado')
'''



# exercicio 8 - Crie um programa que leia um valor em metros e o exiba em centímetros e milímetros.
'''
m = float(input('Escreva uma medida em metros: '))

cm = m * 100

print('Em centímetros, essa medida é de: {} cm'.format(cm))

mm = m * 1000

(print('E em milímetros, essa medida é de: {} mm'.format(mm)))
'''



# exercicio 9 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
'''
n = int(input('Digite um número para visualizar a sua tabuada: '))

contador = 1

while contador <= 100:
      r = n * contador
      print('{} x {} = {}'.format(n, contador, r))
      contador += 1
'''



# exercicio 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
'''
r = float(input('Digite quantos reais você tem no banco: '))

tdc = 4.99

d = r / tdc 
d = round(d, 2)

print('Com esse dinheiro você consegue comprar {}'.format(d))
'''


# exercicio 11 - Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados.

alt = float(input('Digite a altura da parede em metros: '))
larg = float(input('Digite a largura da parede em metros: '))

area = alt * larg

print('A sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(alt, larg, area))

tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))

# exercicio 12 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

v = float(input('Qual é o preço do produto? R$'))

p = v * 5 / 100
d = v - p
d = round(d, 2)

r = (print('Com o desconto o produto sairá por apenas R${}'.format(d)))



# exercicio 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário atual do funcionário {}: R$'.format(nome)))
aumento = salario + (salario * 15 / 100)


print(f'O novo salário do funcionário {nome} passará a ser R${aumento:.2f}!')




# exercicio 14 - Criar um algoritmo que transforme leia uma temperatura em graus Celsius e transforme em Fahrenheit

a = int(input("Se quiser converter a temperatura de graus Celsius para Fahrenheit digite 1,\nmas se quiser converter a temperatura de Fahrenheit para Celsius digite 2: "))
t = int(input("Digite a temperatura que deseja converter: "))


if a == 1:
      f = float((t * 1.8) + 32)
else: 
      a == 2
      c = int((t - 32) * 0.5556)

if a == 1:
      print("Aqui está a temperatura convertida de {}°C para Fahrenheit: {}°F.".format(t, f))
else:
      a == 2
      print("Aqui está a temperatura convertida de {}°F para Celsius: {}°C.".format(t, c))




# exercicio 15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input("Por quantos dias o carro foi alugado?: "))
km = float(input("Quantos Km foram pecorridos?: "))

diaria = float(d * 60)
quilometragem = float(km * 0.15)


preco = float(diaria + quilometragem)

print ("Você deverá pagar o total de R${:.2f}. Sendo R${:.2f} do aluguel e R${:.2f} dos km percorridos.".format(preco, diaria, quilometragem))



