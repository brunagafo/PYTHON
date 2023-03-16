from random import choice
print('\nQuem vai apagar o quadro hoje?\n')
a = str(input('Qual o nome do primeiro aluno? '))
b = str(input('Qual o nome do segundo aluno? '))
c = str(input('Qual o nome do terceiro aluno? '))
d = str(input('Qual o nome do quarto aluno? '))
lista = [a, b, c, d]
print('O(A) aluno(a) selecionado(a) é {}.'.format(choice(lista)))
