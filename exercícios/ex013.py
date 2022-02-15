lar = float(input('Qual a largura? '))
alt = float(input('Qual a altura? '))
area = lar * alt
print('Sua dimensão é de {} x {}, e a sua area tem {}m2.'.format(lar, alt, area))

tinta = area / 2
print('Para pintar esta area, será necessario {} litros de tinta.'.format(tinta))