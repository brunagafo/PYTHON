nome = str(input('Qual é o seu nome? ')).strip().lower()
if nome == 'bruna':
    print('Que nome bonito você tem!')
else:
    print('Que nome normal você tem...')
print('Bom dia, {}!'.format(nome))
# apenas if; o comenado alinhado à esquerda sempre vai acontecer, o indentado só sob condição
