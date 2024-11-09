#Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0

for c in range (1, 501): #poderia fazer: "for c in range (1, 501, 2):, pois assim não precisaria usar a condição if para colocar os números  ímpares na lista"
    if c % 2 != 0 and c % 3 == 0:
          cont += 1
          soma += c

print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))