print('\nO nome tem "Silva"!?\n')
nome = str(input('Digite o nome completo: '))
nome = nome.lower()
print('O nome possui a palavra "Silva"?\nA afirmativa é: {}'.format('silva' in nome))
