# Programa que informa se o número é par ou impar.
from termcolor import colored

num = int(input(colored('Digite um número: ','blue')))
resp = num % 2

if resp == 0:
    print(colored('O número digitado foi {} e ele é par.'.format(num),'yellow'))
else:
    print(colored('O número digitado foi {} e ele é impar.'.format(num),'red'))
