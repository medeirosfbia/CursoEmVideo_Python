#Faça um programa que leia um número de 0 a 9999
# e mostre na tela cada um dos dígitos separados.

n = input("Digite um número de 0 a 9999: ")

for i in range(len(n)):
  print(n[i])