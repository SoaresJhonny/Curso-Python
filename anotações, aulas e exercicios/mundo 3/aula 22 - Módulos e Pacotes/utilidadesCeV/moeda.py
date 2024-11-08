def dobro(preco = 0, formatar = False):
    res = preco * 2
    return res if formatar is False else moeda(res)

def metade(preco = 0, formatar = False):
    res = preco / 2
    return res if formatar is False else moeda(res)

def aumentar(preco = 0, porcentagem = 0, formatar = False):
    res = preco + (preco * porcentagem / 100)
    return res if formatar is False else moeda(res)

def diminuir(preco = 0, porcentagem = 0, formatar = False):
    res = preco - (preco * porcentagem / 100)
    return res if formatar is False else moeda(res)

def moeda(preco = 0, simbolo = 'R$'):
    return f'{simbolo}{preco:.2f}'.replace('.',',')
    
def resumo(preco = 0, taxa_aumento = 0, taxa_diminuir = 0):
    #Coleta de dados
    preco = float(input('Digite o preço: R$'))
    porcentagem_aumentar = input('Digite a porcentagem de aumento: ')
    porcentagem_redução = input('Digite a porcentagem de redução: ')
    while porcentagem_aumentar.isnumeric() == False:
        print('Erro! Digite apenas números.')
        porcentagem_aumentar = input('Digite a porcentagem de aumento: ')
    while porcentagem_redução.isnumeric() == False:
        print('Erro! Digite apenas números.')
        porcentagem_redução = input('Digite a porcentagem de redução: ')

    #convertendo porcentagens para float, para realizar os calculos das funções
    porcentagem_aumentar = float(porcentagem_aumentar)
    porcentagem_redução = float(porcentagem_redução)

    #Resumo que será mostrado para o usuário
    print('-'*40)
    print('RESUMO DO VALOR'.center(40))
    print('-'*40)

    print(f'PREÇO ANALISADO: \t{moeda(preco)}')
    print(f'DOBRO DO PREÇO: \t{moeda(dobro(preco))}')
    print(f'METADE DO PREÇO: \t{moeda(metade(preco))}')
    print(f'{porcentagem_aumentar:.0f}% de aumento: \t{moeda(aumentar(preco, porcentagem_aumentar))}')
    print(f'{porcentagem_redução:.0f}% de redução: \t{moeda(diminuir(preco, porcentagem_redução))}')
    print('-'*40)
    return resumo