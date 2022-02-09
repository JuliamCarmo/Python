a = input('Digite algo: ')
print('O tipo primitivo de {} é da classe:'.format(a), type(a))
print('{} refere-se a um número? '.format(a), a.isnumeric())
print('{} é alfabetico? '.format(a), a.isalpha())
print('{} refere-se a alfanumerico? '.format(a), a.isalnum())
print('{} esta em maiúscula? '.format(a), a.isupper())
print('{} esta em minúscula? '.format(a), a.islower())
print('{} esta capitalizada? '.format(a), a.istitle())

