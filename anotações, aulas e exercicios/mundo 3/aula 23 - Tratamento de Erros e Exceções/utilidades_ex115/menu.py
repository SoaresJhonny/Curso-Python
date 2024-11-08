from time import sleep

options = None
cadastros = []

def menu():
    while True:
        print('-'*40)
        print(f'\033[1;33;40m{"MENU PRINCIPAL":^40}\033[m')
        print('-'*40)

        #mostrar opções
        global options
        print('\033[1;33;40m1.\033[m Cadastrar Uma Pessoa\n\033[1;33;40m2.\033[m Ver Pessoas Cadastradas\n\033[1;33;40m3.\033[m Sair do Sistema')
        print()

        while True:
            try:
                options = int(input('\033[1;33;40mSua Opção: \033[m'))
            except ValueError:
                    print('\033[31mErro! Digite apenas números.\033[m')
                    print()
            else:
                if options not in [1, 2, 3]:
                    print('\033[31mErro! Não há essa opção, digite uma opção válida.\033[m')
                    print()
                else:
                    break
                
        print()

        if options == 1:
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
                cadastros.append(pessoa)
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

        elif options == 2:
            if len(cadastros) == 0:
                print('\033[33mNenhuma pessoa cadastrada ainda. voltando para o Menu Principal...\033[m')
                sleep(1.5)
            else:
                print('\nLista de Cadastros:')

                for index, pessoa in enumerate(cadastros, 1):
                    print(f'\n\033[36mCadastro {index}\033[m:')
                    print('-' * 40)

                    for chave, valor in pessoa.items():
                        print(f'{chave.title()}: {valor}')
                    print('-' * 40)

                voltar = str(input('\033[33mDigite "ok" para voltar para o Menu Principal: \033[m'))
                print()
                print()
        
        else:
            print('\033[33mSaindo do Sistema...\033[m')
            sleep(1.5)
            print('\n\033[32mPrograma encerrado.\033[m')
            exit()
menu()