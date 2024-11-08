def leiaInt(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mErro! Digite um número inteiro válido.\033[m')
            print()
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mPrograma encerrado pelo usuário.\033[m')
            exit()
        else:
            return n1

def leiaFloat(msg):
    while True:
        try:
            n2 = float(input(msg))
        except (TypeError, ValueError):
            print(f'\033[31mErro! Digite um número real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[31mPrograma encerrado pelo usuário.\033[m')
            exit()
        else:
            return n2