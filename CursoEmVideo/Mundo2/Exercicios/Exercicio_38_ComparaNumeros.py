#Crie um programa que receba dois números
# e compare os dois, dizendo se o numero
# A é mauior ou menor que B ou se são iguais#

numeroA = int(input('Digite o número A: '))
numeroB = int(input('Digite o número B: '))

if numeroA>numeroB:
    print('O número ',numeroA, 'é maior que o número', numeroB)
elif numeroB>numeroA:
    print('O número ', numeroB, 'é maior que o número', numeroA)
else:
    print('Os número ', numeroA, 'e', numeroB, 'são iguais')
