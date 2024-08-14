# Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.

p = input('Escreva uma frase: ').lower().strip()

letterA = p.count('a')
firstA = p.find('a')+1
lastA = p.rfind('a')+1

print(letterA)
print(firstA)
print(lastA)