from math import sin, cos, tan, radians
print('\nQual é o seno, cosseno e tangente desse grau?\n')
n = float(input('Grau: '))
seno = sin(radians(n))
cosseno = cos(radians(n))
tang = tan(radians(n))
print('Você escolheu {}°. O seno é de {:.2f}, cosseno {:.2f}, e tangente de {:.2f}.'.format(n, seno, cosseno, tang))
