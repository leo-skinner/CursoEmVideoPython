# Faça um programa que leia um numero de 0 a 9999 e mostre
# na tela cada um dos dígitos separados.
# exemplo: 1834
#  Unidade: 4
# Dezena: 3
# centena: 8
# milhar: 1

import math

from time import sleep

num = int(input('Digite um numero de 0 a 9999: '))
print('Calculando...')
sleep(1.5) #só para dar um charme... :)

# Calculo de unidade:
# Numero dividido por 1,
# pegando seu módulo da divisão por 10 (resto da divisão)
# O mesmo ocorre para os demais, vide abaixo.


u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}' .format(u))
print('dezena: {}' .format(d))
print('centena: {}' .format(c))
print('milhar: {}' .format(m))
