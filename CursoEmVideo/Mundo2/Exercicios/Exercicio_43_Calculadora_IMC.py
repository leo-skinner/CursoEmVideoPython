# Desenvolva uma logica que leia o peso e a altura
# de uma pessoa, calcule seu IMC e mostre seu status
# de acordo com a tabela abaixo:
#
# IMC < 18.5 = Abaixo do Peso
# IMC entre 18.5 a 25 = Peso ideal
# 25 a 30 = Sobrepeso
# 30 a 40 = Obesidade
# Acina de 40 = Obesidade Morbida

print('*'*20)
print('Calculadora de IMC')
print('*'*20)

altura = float(input('Entre com sua altura em cm: '))
peso = float(input('Entre com seu peso em kg: '))

imc = peso/(altura*altura)

print('Seu IMC é', round(imc,2))

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >18.5 and imc <= 25:
    print('Você está no peso ideal')
elif imc > 25 and imc <= 30:
    print('Você está com sobrepeso')
elif imc > 30 and imc <=40:
    print('Você está obeso')
else:
    print('Você tem obesidade mórbida. Procure um endocrinologista.')

