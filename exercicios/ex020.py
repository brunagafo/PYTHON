from random import shuffle
print('Quem vai apresentar primeiro?')
a1 = str(input('Qual o nome do 1° aluno(a)? '))
a2 = str(input('Qual o nome do 2° aluno(a)? '))
a3 = str(input('Qual o nome do 3° aluno(a)? '))
a4 = str(input('Qual o nome do 4° aluno(a)? '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será {}.' .format(lista))
