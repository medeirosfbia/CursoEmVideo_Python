# Criar um programa que leia um numero real qualquer pelo teclado e mostre na tela ele em sua proção inteira

from math import trunc
n = float(input("Digite um número real: "))
print(f'O número digitado foi {n} e sua porção inteira é {trunc(n)}')

# é possível fazer com int também
