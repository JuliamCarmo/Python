from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem SENO de {:.2f}.'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}.'.format(angulo, cosseno))
tan = tan(radians(angulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}.'.format(angulo, tan))
