#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = []
coluna = 1
linha = 1


for v in range(1, 10):
    n = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    coluna += 1
    if coluna == 4:
        coluna = 1
        linha += 1
    matriz.append(n)
    
print()
print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]\n[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]\n[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')