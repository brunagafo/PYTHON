d = float(input('Digite o número de km a viagem terá: '))
if d >= 201:
    print('Sua viagem terá mais que 200 km. ', end='')
    print('A cotação é de R$0,45 por km. O custo da passagem é de R${}.'.format(d * 0.45))
else:
    print('Sua viagem terá {} km. O custo da passagem é de R${}.'.format(d, d*0.5))
# preço = d * 0.45 if d > 200 else d * 0.5 --> condicionamento simplificado