#Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

from utils import moeda

p = float(input('Digite o preço: R$'))
print()

print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')


while True:
    x = str(input('Deseja ver o preço aumentando ou dimuindo um percentual? [S/N]: ')).upper().strip()
    print()
    if x == 'N':
        exit()
    if x not in 'SN':
        print('Opção inválida. Digite "S" para sim ou "N" para não.')
        print()
    else:
        break

porcentagem = int(input('Digite a porcentagem: '))

print(f'Aumentando {porcentagem}%, temos {moeda.aumentar(p, porcentagem, True)}')
print(f'Diminuindo {porcentagem}%, temos {moeda.diminuir(p, porcentagem)}')

print("Fim do programa!")