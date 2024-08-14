# Crie um programa que leia três números e diga qual é o maior e qual é o menor.

# CÓDIGO DIMINUIDO
n = []

for i in range(3):
  n.append(int(input(f'Digite o {i+1}° número: ')))

print(f'O MAIOR número é {max(n)}')
print(f'E o MENOR número é {min(n)}')