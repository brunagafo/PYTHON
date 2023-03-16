print('\nSaturando um nome completo com funções!\n')
nome = str(input('Qual é o seu nome completo? ')).strip()  # não precisa uma segunda variável p/ adc função split
print('Função Upper: {}'.format(nome.upper()))
print('Função Lower: {}'.format(nome.lower()))
length = nome.replace(' ', '')
print('Quantidade de letras do nome: {}'.format(len(length)))
#  OU .format(len(nome) - nome.count(' ')))
length0 = nome.split()[0]
print('Quantidade de letras do primeiro nome: {}'.format(len(length0)))
#  OU .format(nome.find(' ')))
