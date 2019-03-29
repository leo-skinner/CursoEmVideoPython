#Programa que diz se o ano é bissexto.
from datetime import date
from time import sleep
ano = int(input('Digite o ano (Digite 0 para o ano atual): '))

print('calculando...')
sleep(1)

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
