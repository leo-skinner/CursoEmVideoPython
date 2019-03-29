#Elabore um programa que calcule o valor
# a ser pago por um produto considerando:
#
# - A vista: 10% desconto
# - Cartão 1x: 5% desconto
# - Cartão em 2x: normal
# - Cartão em 3x ou mais: 20% juros

produto = float(input('Valor do Produto en R$:'))

print('1- A vista')
print('2- 1x no Cartão de crédito')
print('3- 2x no Cartão de crédito')
print('4- 3x no cartão de crétido')
print('5- 4x no cartão de crédito')

pagar = int(input('Informe a forma de paganento:'))

if pagar == 1:
    total = produto - (produto*10)/100
    print(round(total,2))
elif pagar == 2:
    total = produto - (produto*5)/100
    print(round(total,2))
elif pagar == 3:
    print(round(produto,2))
elif pagar >=4 and pagar <=5:
    total = (produto*20)/100 + produto
    print(round(total,2))
else:
    print('Opção inválida')
