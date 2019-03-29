# Desenvolva um programa que leia:
# Nome, idade e sexo de 4 pessoas.
# No final,  ele retornará:
# 1. A média de idade do grupo;
# 2. Qual é o nome do homem mais velho;
# 3. Quantas mulheres tem menos de 21 anos.

from datetime import date
anoAtual = date.today().year #Define data atual através do sistema.
#Inicializando Variaveis.
somaIdade = 0
mulheresMenores = 0
idadeVelho = 0
nomeVelho = ''
#Inicio do Loop
for p in range (1,5):
    print('---= PESSOA {} =---'.format(p))
    nome = str(input('Nome: ')).strip() #Eliminar espaços no inicio e no fim.
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F):'))
    somaIdade += idade
    if sexo in 'Ff' and idade<21: #O comando in 'Ff' verifica se a variavel está em low ou upcase
        mulheresMenores +=1 #Soma se idade menor de 21.
    if sexo in 'Mm' and p == 1: #Se for o primeiro homem, será o primeiro velho.
        idadeVelho = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > idadeVelho: #Se aparecer outro homem e for mais velho, substitui-se pelo novo.
        idadeVelho = idade
        nomeVelho = nome
#Resultados.
media = somaIdade/p
print('A media das idades digitatas é: {}'.format(media))
print('O homem mais velho se chama {} e ele tem {} anos.'.format(nomeVelho,idadeVelho))
if mulheresMenores > 1:
    print('Temos {} mulheres menores que 21 anos'.format(mulheresMenores))
if mulheresMenores == 1:
    print('Temos {} mulher menor de 21 anos.'.format(mulheresMenores))
else:
    print('Não temos mulhers menores de 21 anos.')
