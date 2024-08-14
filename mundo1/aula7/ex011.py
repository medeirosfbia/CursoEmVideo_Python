# cada litro de tinta pinta 2m^2 (2 metros quadrados)
h = float(input("Digite a altura da parede: "))
w = float(input("Digite a largura da parede: "))
area = h * w
paint = area / 2
print('A área da parede é: {:.2f}m^2\nE a quantidade de tinta necessária para a pintura é: {:.2f}l'.format(area, paint))