print("YET ANOTHER TEXT ADVENTURE!")
print('-'*26)
from time import sleep
nome = input("Qual é o seu nome? ")

print("Olá {}! Esta história é sobre você em outra dimensão...".format(nome))
sleep(2)

print(nome, ', você acorda em um quarto sujo e velho. Um cheiro estranho paira no ar...')
sala1 = str(input('O que fazer ?')).strip().upper()

if sala1 == 'EXA':
    print('Não consigo ver nada')
else:
    print('Não entendi')
