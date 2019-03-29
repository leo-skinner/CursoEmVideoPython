# Faca um prograna que leia um angulo qualquer e mostre
# na tela o valor do seno, cosseno e tangente deste angulo

from math import sin, cos, tan, radians

angulo = float(input('Digite um angulo de 0 a 360 graus: '))

## Radians Converte de graus para radianos.
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O Seno é {:.2f}, o coseno é {:.2f} e a tangente {:.2f}'.format(seno, cosseno, tangente))
