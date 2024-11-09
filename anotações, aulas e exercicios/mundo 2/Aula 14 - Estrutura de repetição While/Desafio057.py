#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'm' ou 'f'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = 0

sexo = str(input('Qual seu sexo? [M/F]: ')).lower()[0]
while sexo not in 'mf':
    print('Essa opção não existe, tente novamente.')
    sexo = str(input('Qual seu sexo? [M/F]: ')).lower()

if sexo == 'm':
    sexo = 'Masculino'
elif sexo == 'f':
    sexo = 'Feminino'
print('Sexo {} registrado com sucesso!'.format(sexo))