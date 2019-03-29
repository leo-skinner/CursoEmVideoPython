# Um professor quer sortear um dos seu quatro alunos para
# apagar o quadro. Faca um programa que ajude ele, leondo
# o nome deles e escrevendo o nome escolhido.

import random

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
print('Os alunos digitados são: ', a1, a2, a3, a4)

escolha = random.choice((a1, a2, a3, a4))

print('O escoliho foi ', escolha)

## Solucao do professor

n1 = str(input('Aluno A: '))
n2 = str(input('Aluno B: '))
n3 = str(input('Aluno C: '))
n4 = str(input('Aluno D: '))

lista = [n1, n2, n3, n4]
sorteio = random.choice(lista)

print('Solucao do professor:')
print('O Aluno escolhido foi: {}'.format(sorteio))
