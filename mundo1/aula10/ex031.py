# Desenvolva um programa que pergunta a distância de uma viagem em Km.
# Calcula o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km
# e R$0.45 para viagens mais longas.

dist = int(input('Informe a distância da viagem em Km: '))

if dist <= 200: price = 0.5
else: price = 0.45

value = price * dist

print('-'*20)
print(f'O valor da viagem será R${value:.2f} pois o preço por Km nesse caso é de R${price:.2f}')