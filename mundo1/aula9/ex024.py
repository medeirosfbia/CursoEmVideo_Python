#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

city = input("Diga o nome da cidade: ").strip()

cityU = city.upper()
if cityU.find("Santo") == 0:
  print(f'O nome da cidade "{cityU}" começa com Santo')
else:
  print(f'O nome da cidade "{cityU}" não começa com Santo')