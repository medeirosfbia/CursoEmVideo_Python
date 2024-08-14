# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = input("Digite seu nome: ")

if "SILVA" in name.upper():
  print(f'Tem "Silva" no nome {name}')
else:
  print(f'Não tem "Silva" no nome "{name}"')