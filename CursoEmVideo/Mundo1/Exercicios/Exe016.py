# Crie um programa que leia um numero real
# qualquer pelo teclado e mostre na tela
# a sua porção inteira.
# Ex: Digite o numero 6.126 e retornará 6 como a parte inteira.


# Forma 1
num = float(input('Digite um numero Real: '))
corte = int(num)

print('A parte inteira de {} é {}.'.format(num, corte))

# Forma 2 (professor)
from math import trunc
n2 = float(input('Digite um valor: '))
print('O valor digitado foi {} e seu inteiro é {}'.format(n2, trunc(n2)))

#Forma 3 (professor)
n3 = float(input('Digite um numero: '))
print('O Valor digitado foi {} e seu inteiro é {}'.format(n3, int(n3)))
