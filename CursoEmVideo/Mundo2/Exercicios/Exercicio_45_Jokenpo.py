# Jokenpo - Pedra, Papel e Tesoura
#
# 1 Pedra >  3 Tesoura
# 3 Tesoura > 2 Papel
# 2 Papel > 1Pedra#
import random

print('-=-'*10)
print('Jokenpo: Pedra, papel ou tesoura')
print('-=-'*10)

print('1- Pedra')
print('2- Papel')
print('3- Tesoura')
player = int(input('Selecione a Opção: '))

choose = [1,2,3]
cpu = random.choice(choose)
print('O CPU escolheu ',  cpu)

if player == cpu:
    print('Empate')
elif player == 1 and cpu == 3 or player == 3 and cpu == 2 or player == 2 and cpu == 1:
    print('Você ganhou')
elif cpu == 1 and player == 3 or cpu == 3 and player == 2 or cpu == 2 and player == 1:
    print('CPU Ganhou')