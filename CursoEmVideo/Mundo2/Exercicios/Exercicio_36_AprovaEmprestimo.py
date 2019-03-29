# Escreva um programa para aprovar
# emprestimo bancario para a compra de
# uma casa. O programa vai perguntar:
# - O valor da casa
# - O salário do comprador
# - Quantos anos serão pagos
#
# Calcule o valor da prestação, sabendo que ela
# não pode exceder 30% do salário ou então o empréstimo será negado.

valImovel = float(input('Valor do Imovel: '))
salario = float(input('Salario: '))
anos = int(input('Prazo em anos: '))

#Converte os anos em meses.
meses = anos * 12

#Testes
print('valor do imovel:', valImovel)
print('salario:', salario)
print('prazo em anos:', anos)
print('prazo em meses:', meses)

valPrestacao = valImovel/meses
print('Valor mensal da Prestação', valPrestacao)

trintaPorcento = (salario*30)/100
print('30% do salário: ', trintaPorcento)

if valPrestacao <= trintaPorcento:
    print('Seu salário é de R$', salario, 'sua parcela será de R$', valPrestacao)
    print('Seu empréstimo foi aprovado.')

else:
    print('Seu salário é de R$', salario, 'sua parcela será de R$', valPrestacao)
    print('Infelizmente, não foi possível aprovar seu empréstimo.')
