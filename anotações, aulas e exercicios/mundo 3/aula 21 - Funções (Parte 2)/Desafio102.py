#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcula o fatorial do número digitado.
    :param num: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: Retorna o valor de n.
    """
    multiplicador = 1
    if show == True:
        for numero in range(num, 0, -1):
            print(numero, end='')
            if numero > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            multiplicador *= numero
        return multiplicador
    if show == False:
        multiplicador = 1
        print('-'*20)
        for numero in range(num, 0, -1):
            multiplicador *= numero
        return multiplicador


print(fatorial(5, True))