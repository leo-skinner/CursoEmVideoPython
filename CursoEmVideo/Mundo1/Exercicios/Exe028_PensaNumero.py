# O CPU pensa em um número de 1 a 5 e vccê deverá advinhar.
import random
from time import sleep

print('Vou te desafiar...')
sleep(1)

numero = random.randint(1,5)

chute = int(input('Em qual número de 1 a 5 estou pensando? '))
print('Processando...')
sleep(1)

if numero == chute:
    print('Parabéns! Você acertou!')
else:
    print('Tente novamente. O número que pensei foi o {}'.format(numero))
