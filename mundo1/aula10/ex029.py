# Escreva um programa que leia a velocidade de um carro.
# Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ela foi multada.
# A multa vai custar R$ 7,00 por cada km acima do limite.

limit = 80
value = 7

x = int(input('Qual a velocidade do carro(Km/h)?\n'))

if x > limit:
  print('***********')
  print('Você foi multado')
  pay = (x - limit) * value
  print(f'O valor da multa é de R${pay:.2f}, pois você estava a {x}Km/h')
  print('***********')
else:
  print('Você está dentro do limite de velocidade')