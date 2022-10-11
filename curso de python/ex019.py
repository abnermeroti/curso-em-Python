from random import choice
a1 = input('digite o nome do aluno1: ')
a2 = input('digite o nome do aluno2: ')
a3 = input('digite o nome do aluno3: ')
a4 = input('digite o nome do aluno4: ')
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print('o aluno escolhido foi: {}'.format(sorteado))