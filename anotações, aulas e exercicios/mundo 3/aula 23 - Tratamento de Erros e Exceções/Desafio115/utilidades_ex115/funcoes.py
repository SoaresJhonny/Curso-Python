def linha(tam=40):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(f'\033[1;33;40m{txt:^40}\033[m')
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'{c}. {i}')
        c += 1
