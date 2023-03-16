from random import choice
tentativa = int(input('Tente adivinhar em qual número eu pensei de 0 à 5: '))
lista = [0, 1, 2, 3, 4, 5]
# OU importar método randint do módulo random e criar numero = randint (0, 5) para não criar lista
numero = choice(lista)
if tentativa == numero:
    print('Você ganhou! O número é {}.'.format(numero))
else:
    print('Sinto muito, você perdeu... O número era {}!'.format(numero))
