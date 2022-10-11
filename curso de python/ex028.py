from random import randint
from time import sleep
computador = randint(0,5) #faz o computador sortear
print('-=-'*10)
print('vou pensar em um numero de 0 a 5, tente adivinhar...')
print('-=-'*10)
jogador = int(input('em que numero eu pensei?'))
print('processando...')
sleep(3)
if jogador == computador:
    print('PARABENS voce adivinhou')
else:
    print('GANHEI! Eu pensei no numero {} e nao no {}'.format(computador, jogador))



