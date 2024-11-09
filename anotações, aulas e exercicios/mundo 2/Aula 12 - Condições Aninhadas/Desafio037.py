#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('CONVERSOR DE BASE NUMÉRICA')
print()
print('BASES:')
print()
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print()

base = int(input('Digite o número da base numérica que você quer converter: '))
numerousuario = int(input('Digite o número que você deseja converter: ')) #será usado para exibir na tela
numerocalculo = numerousuario #será usado para calcular
registro = []
base_nome = 0

#será usado para formatar o ultimo print do código
if base == 1:
    base_nome = 'Binário'
elif base == 2:
    base_nome = 'Octal'
elif base == 3:
    base_nome = 'Hexadecimal'
else:
    print('Não temos essa base, reinicie o programa e tente novamente.')


#binário
if base == 1:
    while numerocalculo != 0:
        resto = numerocalculo % 2
        registro.append(resto)
        numerocalculo = numerocalculo // 2


#octal
if base == 2:
    while numerocalculo != 0:
        resto = numerocalculo % 8
        registro.append(resto)
        numerocalculo = numerocalculo // 8


#hexadecimal
if base == 3:
    while numerocalculo != 0:
        resto = numerocalculo % 16
        if resto < 10:
            registro.append(resto)
        else:
            registro.append(chr(55 + resto)) # Transforma números maiores que 9 em dígitos hexadecimais (A-F)
        numerocalculo = numerocalculo // 16


registro.reverse() #inverte a ordem dos resultados para que seja exibido o resultado correto na tela
resultadofinal = ''.join(map(str, registro)) #transforma os itens da lista em strings
print('o número {} em {} é {}.'.format(numerousuario, base_nome, resultadofinal))