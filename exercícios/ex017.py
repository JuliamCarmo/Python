dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? Km '))
pago = (dias * 60) + (km * 0.33)
print('O total a pagar é de R${:.2f}'.format(pago))