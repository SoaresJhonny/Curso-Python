#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados.

alt = float(input('Digite a altura da parede em metros: '))
larg = float(input('Digite a largura da parede em metros: '))

area = alt * larg

print('A sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(alt, larg, area))

tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))