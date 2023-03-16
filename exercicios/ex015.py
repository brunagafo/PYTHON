print('\nQuanto por um aluguel de carro?\n')
# O carro custa R$60,00 por dia e R$0,15 por km rodado
d = int(input('Dias de aluguel: '))
km = float(input('Km rodados com o carro: '))
valor = (d*60) + (km*0.15)
print('O valor a ser pago pelo aluguel do carro é de R${0:.2f}.'.format(valor))
