from random import shuffle
a1 = input('digite o nome do aluno1: ')
a2 = input('digite o nome do aluno2: ')
a3 = input('digite o nome do aluno3: ')
a4 = input('digite o nome do aluno4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('a ordem sera: ')
print(lista)