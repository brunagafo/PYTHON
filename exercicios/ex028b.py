from random import randint
from time import sleep
print('~~~'*17)
print('Estou pensando em um número entre 1 e 5...')
print('~~~'*17)
tentativa = int(input('Tente adivinhar em qual número eu pensei! '))
numero = randint(1, 5)
print('~~~'*17)
print('PROCESSANDO...')
sleep(2)
if tentativa == numero:
    print('PARABÉNS!!! Você ganhou, O número é {}.'.format(numero))
else:
    print('Sinto muito, você perdeu... O número era {}!'.format(numero))
