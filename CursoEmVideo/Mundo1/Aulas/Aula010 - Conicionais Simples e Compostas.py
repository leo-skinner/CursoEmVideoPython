from time import sleep
nome = str(input('Qual o seu nome? ')).title()

sleep(1)

# Estrutura simples.
if nome == 'Leonardo':
    print('Seu nome é o melhor do mundo!')
print('Bom dia, {}!'.format(nome))

sleep(1)
# Estrutura composta
carro = int(input('Qual a idade de seu carro? '))
if carro <=3:
    print('Seu carro é novo!')

else:
    print('Já pensou em trocar essa lata-velha?')

sleep(1)
print('Seu nome é {} e seu carro tem {} anos.'.format(nome, carro))

#Verificando média...
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))

m = (n1+n2)//2

print('Calculando média...')
sleep(1)
if m >=6:
    print('Parabéns {}! Você passou de ano.'.format(nome))
else:
    print('Teremos que nos encontrar no ano que vem {}. VocÊ foi reprovado.'.format(nome))

print('{}, sua média foi {}.'.format(nome,m))
print('')
print('')
sleep(1)
print('Utilizando um if simplificado...')
sleep(1)

# utilizando o if somplificado.
idade = int(input('{}, qual a sua idade ?'.format(nome)))
sleep(1)
print('Olá vovô' if idade>60 else print('Oi cocota!'))
