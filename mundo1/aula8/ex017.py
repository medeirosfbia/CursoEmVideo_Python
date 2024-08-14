# Triangulo retângulo

from math import hypot
side1 = float(input("Digite o comprimento do cateto oposto do triângulo: "))
side2 = float(input("Digite o comprimento do cateto adjacente do triângulo: "))
print(f'A hipotenusa vai medir {hypot(side1, side2):.2f}')