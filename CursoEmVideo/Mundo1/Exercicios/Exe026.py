#Programa que leia uma frase digitada e mostre:
#
# - Quantas vezes aparece a letra 'A'
# - Em qual posição ela aparece a primeira vez.
# - Em qual posição aparece pela última vez.

frase = input('Digite uma frase: ').strip().lower()

print('Sua frase possui {} letras A.'.format(frase.count('a')))
print('Sua frase ocupa {} posições na memória' .format(len(frase)))
print('A letra A aparece na posição {} pela primeira vez'.format(frase.find('a')+1))
print('A letra A aparece pela última vez na posição {}'.format(frase.rfind('a')+1))
