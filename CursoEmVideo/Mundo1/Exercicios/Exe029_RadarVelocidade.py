#Programa de radar
#Limite de velocidade: 80km/h
#Cálculo de multa: R$7,00 por km acima do limite.

from time import sleep
import colorama

colorama.init()

print(colorama.Fore.BLUE + '-=-'*7)
vel = float(input('Digite a velocidade: '))
multa = (vel-80)*7
sleep(1)

if vel <= 80:
    print('Seu carro passou a {}km/h. Você está dentro do limite.'.format(vel))
else:
    print('Seu carro passou a {}km/h. infelizmente vocÊ foi multado em {} Reais.'.format(vel,multa))

sleep(1)
print('Detran-RJ.')
print('Criando dificuldade, para vender facilidade!')
