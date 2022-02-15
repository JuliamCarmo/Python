real = float(input('Quantos reais você deseja converter? R$'))
dolar = real / 5.18
euro = real / 5.89
print('Com {:.2f} reais, você obtem {:.2f} dolares e {:.2f} euros.'.format(real, dolar, euro))
