# Crie um programa que leia um ano qualquer e diga se é bissexto.

# se o número formado pelos dois últimos algarismos
# do referido ano for múltiplo de 4,
# este ano é bissexto

from datetime import datetime

y = int(input('Digite o ano, coloque 0 para analisar o ano atual...\n '))
y = datetime.now().year if y == 0 else y

d400 = y % 400
d4 = y % 4
d100 = y % 100

if d400 == 0 or (d4 == 0 and d100 != 0):
  print(f'O ano {y} é um ano BISSEXTO')
else:
  print(f'O ano {y} NÃO é um ano BISSEXTO')


