# Aumento de salário
# Salarios superiores a 1.250,00 - 10%
# Salarios inferiores - 15%
from time import sleep

nome = str(input('Digite seu nome: '))
sleep(1)
salario = float(input('Olá, {}. Digite seu salário: '.format(nome)))

if salario <= 1250:
    print('Você teve um reajuste de 15% - R${}'.format(((salario*15)//100)+salario))
else:
    print('Você teve um reajuste de 10% - R${}'.format(((salario*10)//100)+salario))
