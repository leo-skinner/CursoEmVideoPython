# O mesmo professor quer sortear a ordem de apresentacao
# de trabalho dos alunos. Faca um programa que leia o nome
# dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1, a2, a3, a4]

shuffle(lista)
print('A seguencia é: ', lista)
