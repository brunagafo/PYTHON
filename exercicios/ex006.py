print('Digite aqui um número e irei lhe mostrar o dobro, triplo e raíz quadrada!')
n = int(input('Digite um número: '))
print('O dobro de {} é {}.\nO triplo de {} é {}.\n'.format(n, (n*2), n, (n*3), n))
print('A raíz quadrada de {} é {:.2f}.' .format(n, pow(n, (1/2))))
