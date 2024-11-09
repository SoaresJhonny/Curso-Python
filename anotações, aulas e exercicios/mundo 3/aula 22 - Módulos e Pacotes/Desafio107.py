#exercicio 107 - Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar, diminuir, dobro e metade. Faça também um programa que importe esse módulo e use algumas dessas funções.

from utils import moeda

p = float(input('Digite o preço: R$'))
print()

print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'A metade de {p} é {moeda.metade(p)}')


while True:
    x = str(input('Deseja ver o preço aumentando ou dimuindo uma porcentagem? [S/N]: ')).upper().strip()
    print()
    if x == 'N':
        exit()
    if x not in 'SN':
        print('Opção inválida. Digite "S" para sim ou "N" para não.')
        print()
    else:
        break

porcentagem = int(input('Digite a porcentagem: '))

print(f'Aumentando {porcentagem}%, temos {moeda.aumentar(p, porcentagem)}')
print(f'Diminuindo {porcentagem}%, temos {moeda.diminuir(p, porcentagem)}')

print("Fim do programa!")
