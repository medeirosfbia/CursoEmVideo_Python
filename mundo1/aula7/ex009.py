n = int(input("Digite um número inteiro: "))
print('-'*20)
print(f"A tabuada do número {n} é:")
for i in range(1, 11):
  print(f'{n} x {i} = {n*i}')
print('-'*20)