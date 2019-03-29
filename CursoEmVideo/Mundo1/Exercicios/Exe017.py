# Faça um programa que leia o comprimento do cateto oposto e do adjacente
# de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

oposto = float(input('Entre com o valor do cateto oposto: '))
adjacente = float(input('Entre com o valor do cateto adjacente: '))

hipotenusa = hypot(oposto, adjacente)

print('O valor da hipotenusa é: {:.2f}' .format(hipotenusa))

## Forma matemática
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co **2 + ca **2) ** (1/2)

print('O Cateto oposto digitado foi {}, o adjacente {} e a hipotenusa é {:.2f}'.format(co, ca, hi))
