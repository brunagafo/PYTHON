from math import hypot
print('\nCalculando a hipotenusa!\n')
ca = float(input('Comprimento do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))
print('A hipotenusa do triângulo retângulo de catetos {} x {} é {:.2f}'.format(ca, co, hypot(ca, co)))
