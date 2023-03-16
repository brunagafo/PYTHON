n = float(input('Qual é o seu salário? '))
if n >= 1250:
    novo = n * 110 / 100
else:
    novo = n * 115 / 100
print('Seu salário de R${:.2f} passa a ser de R${:.2f}.'.format(n, novo))
