#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Escreva o nome da cidade em que você nasceu: ')).strip()

cidade = cidade.lower()
print(cidade[:5] == 'santo')