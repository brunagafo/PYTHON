print('Reajuste Salarial.\nDigite o valor do seu salário atual para saber o valor do seu novo salário.\n')
s = float(input('Valor do salário atual: R$ '))
n = s * 115 / 100
print('O seu salário terá aumento de 15%. O novo valor é de R$ {:.2f}.' .format(n))
