# Escreva um programa que leia um inteiro
# e peça para que o usuário escolha a conversão
# 1- binário
# 2- Octal
# 3- HexaDecimal
import time
import cmath

numero = int(input('Digite um número qualquer: '))
time.sleep(1)

print('Escolha a conversão:')
print('1- Binário')
print('2- Octal')
print('3- Hexadecimal')

conversor = int(input('Escolha uma opção: '))

print('pensando...')
time.sleep(1)

if conversor == 1:
    binario = bin(numero)[2:]
    print('O numero', numero, 'convertido em binário é:', binario)

elif conversor == 2:
    octa = oct(numero)[2:]
    print('O numero', numero, 'convertido em octa é:', octa)

elif conversor == 3:
    hexadecimal = hex(numero)[2:]
    print('O numero', numero, 'convertido em hexa é: ', hexadecimal)

else:
    print('Você digitou um número inválido!')