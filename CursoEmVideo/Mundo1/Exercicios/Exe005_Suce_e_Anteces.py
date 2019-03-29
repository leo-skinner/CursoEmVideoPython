# Faça um programa que leia um
# número inteiro e mostre na tela
# seu sucessor e antecessor

from time import sleep

fim = ''

while fim != 'S' and fim != 'N':
    fim = 'S'
    print('\033[32mxX\033[m'*11)
    print('Sucessor e antecessor')
    print('\033[32mxX\033[m'*11)
    print()

    num = int(input('\033[33mDigite um número inteiro: \033[m'))

    print("\033[34mO numero digitado foi {}\nSeu antecessor é {}\n\033[35mSeu sucessor é {}\033[m" .format(num,(num-1),(num+1)))

    fim = str(input('Outra vez? (S/N): ')).upper()
var = fim == 'N'
print('Até logo!')
