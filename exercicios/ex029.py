n = float(input('Velocidade do carro em km/h: '))
print('O motorista atingiu {} km/h.'.format(n))
if n > 80.0:
    print('A velocidade está acima do permitido. O proprietário do veículo será multado!')
    print('O valor da multa será de R${:.2f}.'.format((n - 80) * 7))
else:
    print('A velocidade do veículo está dentro do limite permitido por lei.')
