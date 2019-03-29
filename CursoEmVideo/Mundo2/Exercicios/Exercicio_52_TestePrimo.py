# Faça um programa que leia um número
# inteiro e diga se ele é primo ou não.#
testePrimo = int(input('Digite um numero para testar se ele é primo: '))
tot = 0
for c in range(1,testePrimo+1):
    if testePrimo%c == 0:
        print('\033[33m', end=' ')
        tot +=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(testePrimo, tot))
if tot == 2:
    print('Ele é primo')
else:
    print('Ele não é primo')
