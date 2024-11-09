#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input("Por quantos dias o carro foi alugado?: "))
km = float(input("Quantos Km foram pecorridos?: "))

diaria = float(d * 60)
quilometragem = float(km * 0.15)


preco = float(diaria + quilometragem)

print ("Você deverá pagar o total de R${:.2f}. Sendo R${:.2f} do aluguel e R${:.2f} dos km percorridos.".format(preco, diaria, quilometragem))