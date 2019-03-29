# Programa que leia o nome completo de uma pessoa e mostre:
# - Primeiro e último nome.
# Exemplo: Ana Maria Braga da Silva
# Primeira: Ana
# Última: Silva
from time import sleep
nome = input('Digite seu nome Completo: ').strip()

nomeLista = nome.split()

print('Seu primeiro nome é: {}'.format(nomeLista[0]))
print('Seu último nome é: {}'.format(nomeLista[-1]))

print('soluçao do professor...')
sleep(1.5)

print('usando nomeLista[len(nomeLista)-1] - {}' .format(nomeLista[len(nomeLista)-1]))
