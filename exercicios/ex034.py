n = float(input('Qual é o seu salário? '))
if n >= 1250:
    print('Seu novo salário tem 10% de acréscimo e é de R${:.2f}.'.format(n * 110 / 100))
else:
    print('Seu salário tem 15% de acréscimo e é de R${:.2f}.'.format(n * 115 / 100))
