print('Quantos dólares eu consigo comprar?\n')
real = float(input('Quantos Reais você têm? (Separe os centavos por um ponto "."): R$ '))
dolar = real / 5.28
print('Com R${:.2f} reais, você consegue US${:.2f} dólares!' .format(real, dolar))
print('\nEste valor de conversão é válido para 18/10/2022.')
