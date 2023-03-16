print('\nPagamento à vista e à prazo!\n')
# O pagamento a vista tem 10% de desconto, e a prazo tem 8% de juros totais.
n = float(input('Valor do produto: R$ '))
v = n * 90 / 100
p = n * 108 / 100
print('O valor do produto é de R$ {:.2f}. À vista R$ {:.2f}. À prazo R$ {:.2f}.'.format(n, v, p))
