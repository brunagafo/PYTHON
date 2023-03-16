print('\nNome da cidade: Começa com "Santo"?\n')
cidade = str(input('Qual é o nome da sua cidade? ')).strip()
conversao = cidade.lower().split()[0]
print('O nome da sua cidade começa com santo? A resposta é: {}.' .format('santo' in conversao))
#  print(cidade[:5].lower() == 'santo')
