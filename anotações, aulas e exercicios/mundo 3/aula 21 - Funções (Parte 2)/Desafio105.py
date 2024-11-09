#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)

# Adicione também as docstrings da função.

def notas(*nts, sit=False):
    """
    -> Recebe quantidade de notas variáveis e calcula a quantidade total de notas, a maior nota, a menor nota, a média e a situação geral da turma.
    :param *nts: As notas que serão verificadas (Aceita várias)
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Print com várias informações sobre a situação da turma.
    """

    maior_nota = max(nts)
    menor_nota = min(nts)
    media = sum(nts) / len(nts)
    
    if media >= 8.0:
        situação = 'Boa'
    elif media < 8.0 and media >= 6.0:
        situação = 'Razoável'
    else:
        situação = 'Ruim'

    if sit == False:
        return f'Total: {len(nts)}  Maior: {maior_nota} Menor: {menor_nota}  Média: {media:.2f}'
    else:
        return f'Total: {len(nts)}  Maior: {maior_nota}  Menor: {menor_nota}  Média: {media:.2f}  Situação: {situação}'

#programa principal
resp = notas(5.0, 9.5, 7.0, 8.5, 6.5, 2.0, sit=True)
print(resp)