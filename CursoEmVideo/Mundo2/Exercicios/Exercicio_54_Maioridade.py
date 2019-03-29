#Crie um programa que leia o ano de nascimento
# de 7 pessoas. No final, mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já
# são maiores.#
from datetime import date
anoAtual = date.today().year
totalMaior=0
totalMenor=0
for pess in range(1,8):
    nasc = int(input('Digite o ano da {} pessoa: '.format(pess)))
    idade = anoAtual - nasc
    print('Essa pessoa tem {} anos'.format(idade))
    if idade >=18:
        totalMaior += 1
    else:
        totalMenor +=1
print('Temos um total de {} menores e {} maiores.'.format(totalMenor,totalMaior))
