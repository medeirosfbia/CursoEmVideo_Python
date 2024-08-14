m = float(input("Digite o valor em metros: "))
dist = [m/1000,m/100,m/10,m*10,m*100,m*1000]
name = ['km','hm','dam','dm','cm','mm']
print(f'A medida de {m:.1f}m corresponde a:')
for i in range(0, len(dist)):
  print(f'{dist[i]}{name[i]}')