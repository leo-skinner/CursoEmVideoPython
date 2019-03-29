#A Confederacao Nacional de Natacao precisa de um programa
# que leia o ano do nascimento de um atleta e mostre sua categoria
# de acordo com a idade:
#
# - até 9 anos = Mirim
# - até 14 anos = Infantil
# - até 19 anos = Junior
# - até 20 anos = Senior
# - acima = Master

anoAtual = int(input('Digite o ano atual: '))
anoNascimento = int(input('Digite o ano do seu nascimento: '))

idade = anoAtual - anoNascimento

print('Estamos no ano de ', anoAtual, 'e você tem ',idade, 'anos')

if idade <= 9:
    print('Sua categoria é Mirim')
elif idade > 9 and idade <= 14:
    print('Sua categoria é Infantil')
elif idade > 14 and idade <= 19:
    print('Sua categoria é Junior')
elif idade > 19 and idade <= 20:
    print('Sua categoria é Senior')
else:
    print('Sua categoria é Master')