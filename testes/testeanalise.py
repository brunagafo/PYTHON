frase = 'Curso em Vídeo Python'
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android'))
print('Curso' in frase)  # Se existe a palavra dentro da variável - booleano
print(frase.find('Vídeo'))  # Mostra a posição de caractere onde começa a palavra
print(frase.lower().find('vídeo'))  # Transforma a string em letras minúsculas antes de realizar busca
