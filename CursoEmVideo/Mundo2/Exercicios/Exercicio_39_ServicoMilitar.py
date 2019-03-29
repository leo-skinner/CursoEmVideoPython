# Faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar no serviço militar;
# - Se é a hora de se alistar;
# - Se já passou do tempo de alistamento.
# O programa deverá mostrar o tempo que falta ou
# o tempo que já passou, após o prazo de alistamento.#
from datetime import date

anoAtual = date.today().year
sexo = str(input('Sexo M ou F: '))

if sexo == 'F' or sexo == 'f':
    print('Você não precisa se alistar')
    exit()
elif sexo !='F' or sexo != 'f' or sexo != 'm' or sexo !='M':
    print('Selecione uma opção válida!')
    exit()
else:
    anoNasc = int(input('Ano de Nascimento: '))

idade = anoAtual-anoNasc

if idade == 18:
    print('Você tem ', idade, 'anos. Está na hora de servir a pátria.')
elif idade < 18:
    print('Você tem ', idade, 'anos. Ainda faltam ' ,18-idade, 'anos para se alistar')
else:
    print('Você tem', idade, 'anos. Você já deveria ter se alistado a ',idade-18, 'anos')
