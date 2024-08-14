# Crie um programa que leia três números e diga qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

max = n1
min = n1

#MAIOR
if n2 > n1 and n2 > n3:
  max = n2
if n3 > n1 and n3 > n2:
  max = n3

#MENOR
if n2 < n1 and n2 < n3:
  min = n2
if n3 < n1 and n3 < n2:
  min = n3

print(f'O MAIOR número é {max}')
print(f'E o MENOR número é {min}')
