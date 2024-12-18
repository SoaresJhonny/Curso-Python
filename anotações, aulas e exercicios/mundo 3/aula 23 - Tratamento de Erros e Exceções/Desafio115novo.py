from time import sleep
from Desafio115.utilidades_ex115.funcoes import *
from Desafio115.ArquivodeCadastros.arquivo import arqExiste, arqCriar

arq = 'Cadastros Python'

if not arqExiste(arq):
    arqCriar(arq)

while True:
    options = menu(['Cadastrar Uma Pessoa', 'Ver Pessoas Cadastradas', 'Sair do Sistema'])
    try:
        option = int(input('\n\033[1;33;40mSua Opção: \033[m'))
    except ValueError:
        print('\033[31mErro! Digite apenas números.\033[m')
        print()
    else:
        if options not in [1, 2, 3]:
            print('\033[31mErro! Não há essa opção, digite uma opção válida.\033[m')
            print()
        else:
            break

    if option == 1:
            while True:
                print('Preencha os campos a seguir: ')
                print()

                pessoa = {}
                
                pessoa['nome'] = input('\033[1;33;40mNome: \033[m').title()
                while pessoa['nome'].isnumeric() == True:
                    print('\033[31mErro! No campo "Nome" digite apenas letras.')
                    print()
                    pessoa['nome'] = input('\033[1;33;40mNome: \033[m').title()

                pessoa['idade'] = input('\033[1;33;40mIdade: \033[m')
                while pessoa['idade'].isalpha() == True:
                    print('\033[31mErro! No campo "Idade" digite apenas números.')
                    print()
                    pessoa['idade'] = (input('\033[1;33;40mIdade: \033[m'))

                print('\n\033[32mPessoa cadastrada com Sucesso!\033[m')
                print()

                while True:
                    continuar = str(input('Deseja cadastrar mais uma pessoa? [S/N]: ')).upper()

                    if continuar not in ['S', 'N']:
                        print('\033[31mErro! Digite "S" para "Sim" ou "N" para "Não".\033[m')
                        print()
                    else:
                        break

                if continuar == 'N': #Sai do loop externo
                    print('\n\033[33mVoltando para o Menu Principal...\033[m')
                    sleep(1.5)
                    print()
                    break


