#Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado

from utils import moeda

p = float(input('Digite o preço: R$'))
print()

print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')


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

print(f'Aumentando {porcentagem}%, temos {moeda.moeda(moeda.aumentar(p, porcentagem))}')
print(f'Diminuindo {porcentagem}%, temos {moeda.moeda(moeda.diminuir(p, porcentagem))}')

print("Fim do programa!")
