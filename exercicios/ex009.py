
print('Digite um número e eu te darei a tabuada dele!')

n = int(input('Qual é o número? '))
print('\nVocê escolheu o número {}! Esta é a a tabuada: '.format(n))
print('---------- \n {}x1 = {}\n {}x2 = {}\n {}x3 = {}\n {}x4 = {}'.format(n, n*1, n, n*2, n, n*3, n, n*4, n*5))
print(' {}x5 = {}\n {}*6 = {}\n {}*7 = {}\n {}*8 = {}\n {}x9 = {}'.format(n, n*5, n, n*6, n, n*7, n, n*8, n, n*9,))
print(' {}x10 = {}\n----------'.format(n, n*10))

print('\n')

print('-' * 12)
print('{} x {:2} = {:2}' .format(n, 1, n*1))
print('{} x {:2} = {:2}' .format(n, 2, n*2))
print('{} x {:2} = {:2}' .format(n, 3, n*3))
print('{} x {:2} = {:2}' .format(n, 4, n*4))
print('{} x {:2} = {:2}' .format(n, 5, n*5))
print('{} x {:2} = {:2}' .format(n, 6, n*6))
print('{} x {:2} = {:2}' .format(n, 7, n*7))
print('{} x {:2} = {:2}' .format(n, 8, n*8))
print('{} x {:2} = {:2}' .format(n, 9, n*9))
print('{} x {:2} = {:2}' .format(n, 10, n*10))
print('-' * 12)
