# SENO, COSSENO E TANGENTE

from math import sin, cos, tan, radians
n = int(input("Digite um ângulo qualquer: "))

print(f'Seno: {sin(radians(n)):.2f}')
print(f'Cosseno: {cos(radians(n)):.2f}')
print(f'Tangente: {tan(radians(n)):.2f}')
