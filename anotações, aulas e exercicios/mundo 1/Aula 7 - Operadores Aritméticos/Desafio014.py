#Criar um algoritmo que transforme leia uma temperatura em graus Celsius e transforme em Fahrenheit

a = int(input("Se quiser converter a temperatura de graus Celsius para Fahrenheit digite 1,\nmas se quiser converter a temperatura de Fahrenheit para Celsius digite 2: "))
t = int(input("Digite a temperatura que deseja converter: "))

if a == 1:
      f = float((t * 1.8) + 32)
else: 
      a == 2
      c = int((t - 32) * 0.5556)

if a == 1:
      print("Aqui está a temperatura convertida de {}°C para Fahrenheit: {}°F.".format(t, f))
else:
      a == 2
      print("Aqui está a temperatura convertida de {}°F para Celsius: {}°C.".format(t, c))