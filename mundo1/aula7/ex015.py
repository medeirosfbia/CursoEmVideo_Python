# carro custa R$60 por dia e R$0,15 por Km rodado
d = float(input('Quantos Km(quilômetros) rodados? '))
day = int(input('Quantos dias alugados? '))
print(f'O total a pagar é de R${day * 60 + d * 0.15:.2f}')