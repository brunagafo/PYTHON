from emoji import emojize
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua nota média é {}.'.format(m))
if m >= 6.0:
    print('Sua média é boa, parabéns!')
else:
    print(emojize('Sua média foi RUIM! :thumbsdown: :pensive:', language='alias'))
