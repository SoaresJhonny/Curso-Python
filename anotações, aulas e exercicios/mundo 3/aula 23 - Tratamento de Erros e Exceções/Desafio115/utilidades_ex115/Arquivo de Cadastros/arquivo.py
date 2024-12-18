def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def arqCriar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mErro ao criar o arquivo!\033[m')
    else:
        print(f'\033[32mArquivo "{arq}" Criado!\033[m')