#Crie umprograma onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.


n = [[], []]
c = 1

for v in range(1, 8):
    v = int((input(f'Digite o {c}º valor: ')))
    if v % 2 == 0:
        n[0].append(v)
    else:
        n[1].append(v)
    c += 1

if len(n[0]) > 0:
    print(f'Os números pares digitados foram: {sorted(n[0])}')
if len(n[1]) > 0:    
    print(f'Os números ímpares digitados foram: {sorted(n[1])}')