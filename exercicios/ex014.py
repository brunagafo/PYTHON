print('\nConvertendo a temperatura!\n')
c = float(input('Digite a temperatura a ser convertida em °C: '))
print('{0:.1f}°C equivalem a {1:.1f}°F.'.format(c, (c * 1.8 + 32)))
# Dentro das chaves é possível colocar {0}, {1}, {2}... Que equivalem à ordem do .format(0, 1, 2)
