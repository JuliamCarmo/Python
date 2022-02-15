preço = float(input('Qual o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('O produta que custava R${:.2f}, com o desconto de 5% custará R${:.2f}'.format(preço, novo))
