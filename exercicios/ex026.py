print('\nTem letra "A" aqui!?\n')
frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra "A" aparece {} vezes na sua frase.'.format(frase.count('a')))
print('A primeira vez que a letra "A" aparece é na posição {}.'.format(frase.find('a') + 1))
# +1 porque o phyton começa no 0
print('A última vez que a letra "A" aparece é na posição {}.'.format(frase.rfind('a') + 1))
