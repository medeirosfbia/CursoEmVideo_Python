# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

name = (input("Digite seu nome completo: ").strip()).split()

print(name[0])
print(name[-1])