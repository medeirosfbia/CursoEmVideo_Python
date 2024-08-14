#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

name = input("Escreva seu nome completo: ").strip()

print(name.upper())
print(name.lower())

nameLen = len(name) - name.count(" ")
print(f'O tamanho do seu nome é {nameLen}')

fName = name[:name.find(" ")]
fNameLen = len(name[:name.find(" ")])
print(f'Seu primeiro nome é {fName} e ele tem {fNameLen} letras')