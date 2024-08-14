# Programa para calcular o aumento de salário de um funcionário
# Descrição:
# Este programa solicita ao usuário o salário de um funcionário e calcula o valor do seu aumento.
# O aumento é determinado por uma regra simples:
# Para salários superiores a R$1.250,00, o aumento é de 10%.
# Para salários inferiores ou iguais a R$1.250,00, o aumento é de 15%.

value = float(input('Digite o salário: R$'))

if value > 1250.00:
  tax = 1.10
else:
  tax = 1.15

print(f'Quem ganhava R${value:.2f} passa a ganhar R${value * tax:.2f}.')