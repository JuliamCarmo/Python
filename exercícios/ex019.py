from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A medida da hipotenusa é de {:.2f}.'.format(hi))

#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A medida da hipotenusa é de {:.2f}.'.format(hi))