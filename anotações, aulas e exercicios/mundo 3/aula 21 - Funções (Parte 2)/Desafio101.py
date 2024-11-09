#Crie um programa que tenha uma função chamda voto() que vai receber como parâmetro o ano de nascimetno de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

from time import sleep 

print('Verificação de Voto\nPara descobrir se pode votar, respondar as perguntas abaixo:')
sleep(1.6)
print()

def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    
    if idade < 16:
        return f'Com {idade} anos: Não pode votar!'

    while True:
        alf = str(input('É alfabetizado(Sabe ler e escrever)? [S/N]: ')).strip().upper()
        print()
        if alf in 'SN':
            break
        else: 
            print()
            print('Opção inválida! Digite S (Sim) ou N (Não).')
        print()


    if alf == 'S':
        if idade >= 16 and idade < 18:
            return f'Com {idade} anos: Voto Opcional!'
        elif idade >= 18 and idade < 70:
            return f'Com {idade} anos: Voto Obrigatório!'
        elif idade >= 70:
            return f'Com {idade} anos: Voto Opcional!'
        
    elif alf == 'N':
        if idade >= 16:
            return f'Com {idade} anos sendo analfabeto: Voto Opcional!'
        else:
            return f'Com {idade} anos: Não pode votar!'
    

#programa principal
ano_nascimento = int(input('Digite o ano de nascimento: '))
print(voto(ano_nascimento))