medida = float(input('Digite  o valor de uma medida em METROS: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {} metros, corresponde a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm.'.format(medida, km, hm, dam, dm, cm, mm))
