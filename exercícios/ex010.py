med = float(input('Digite  o valor de uma medida em METROS: '))

print('A medida de {} metros, corresponde a:'.format(med))
print('\n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm.'.format(med/1000, med/100, med/10, med*10, med*100, med*1000))

#km = med / 1000, hm = med / 100, dam = med / 10, dm = med * 10, cm = med * 100, mm = med * 1000