#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

vm = 80
v = int(input('Digite a velocidade atual do carro: '))


if v > vm:
    diferenca = v - vm
    m = 7 * diferenca
    print('Você foi multado por exceder a velocidade máxima de 80Km/h || VALOR DA MULTA: R${:.2f}'.format(m).replace('.', ','))