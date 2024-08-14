# Desenvolva um programa que leia o comprimento de três
# retas e diga ao usuário se elas podem ou não formar um triângulo.

# Desigualdade triangular -- A soma de quaisquer dois lados de um triângulo 
# deve ser maior que o comprimento do terceiro lado

def analisador_de_triangulos():
  print('-='*20)
  print('Analisador de Triângulos')
  print('-='*20)

  r = []
  for i in range(3):
    r.append(float(input(f'Digite o comprimento do {i+1}° segmento de reta: ')))

  if r[0] + r[1] > r[2] and r[0] + r[2] > r[1] and r[1] + r[2] > r[0]:
    print('Os segmentos acima PODEM FORMAR triângulo.')
  else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo.')

analisador_de_triangulos()