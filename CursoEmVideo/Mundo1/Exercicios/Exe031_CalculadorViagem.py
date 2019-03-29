# Calcula viagem
# Viagem até 200km - R$0,50
# Viagem mais longa - R$0,45
from time import sleep

print('Calcula Viagens - Tabajara')
print('='*26)
print('')

viagem = float(input('Digite a distância em Km: '))

if viagem <= 200:
    print('O Valor da passagem é de R${:.2f}'.format(viagem*.50))
else:
    print('O valor da passagem é de R${:.2f}'.format(viagem*.45))
sleep(1)
print('Tenha uma boa viagem!')
