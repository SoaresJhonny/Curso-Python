#exercicio 113 - Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

from utils import tipo


numint = tipo.leiaInt('Digite um número inteiro: ')
print()
numfloat = tipo.leiaFloat('Digite um número real: ')

print(f'O número inteiro {numint} e o número real {numfloat} foram digitados com sucesso!')
