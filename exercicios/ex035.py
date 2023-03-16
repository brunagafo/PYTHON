a = float(input('Digite o tamanho da primeira reta: '))
b = float(input('Digite o tamanho da segunda reta: '))
c = float(input('Digite o tamanho da terceira reta: '))
if a < c + b and b < a + c and c < a + b:
    print('As retas de tamanho \033[34m{}\033[m, \033[33m{}\033[m e \033[31m{}\033[m'.format(a, b, c), end='')
    print(' podem formar um triângulo.')
else:
    print('A soma das duas retas de menor tamanho não permite que essas retas formem um triângulo!')
