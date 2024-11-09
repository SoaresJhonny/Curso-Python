#Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

matriz = []
coluna = 1
linha = 1
somapares = somatres = maiorvalor = 0

for v in range(1, 10):
    n = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
    coluna += 1
    if coluna == 4:
        coluna = 1
        linha += 1
    matriz.append(n)
    
print()
print(f'[ {matriz[0]} ] [ {matriz[1]} ] [ {matriz[2]} ]\n[ {matriz[3]} ] [ {matriz[4]} ] [ {matriz[5]} ]\n[ {matriz[6]} ] [ {matriz[7]} ] [ {matriz[8]} ]')

print()
for numero in matriz:
    if numero % 2 == 0:
        somapares += numero
print(f'A soma dos valores pares é {somapares}.')

somatres = matriz[2] + matriz[5] + matriz[8]
print(f'A soma dos valores da terceira coluna é {somatres}.')

maiorvalor = max(matriz[3], matriz[4], matriz[5])
print(f'O maior valor da segunda linha é {maiorvalor}.')