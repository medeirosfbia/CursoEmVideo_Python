# Escreva um programa que faça o computador "pensar"
# em um número inteiro entre 0 a 5 a peça
# para o usuário tentar descobrir qual foi o número escolhido palo computador.

# O programa devará escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
num = randint(0,5)

print('-'*20)
print('Estou pensando em um número entre 0 e 5... Eu te desafio a adivinhar qual número eu estou pensando.')
print('-'*20)
x = int(input('Tente um número, você só tem uma tentativa: '))

print('Processando...')
sleep(3)
if x == num:
  print(f'PARABÉNS! Você acertou, o número era {num}')
else:
  print(f'Que pena, você errou, o número era {num}')