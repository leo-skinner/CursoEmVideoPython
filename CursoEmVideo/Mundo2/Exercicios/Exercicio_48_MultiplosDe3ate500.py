#Faça um programa que calcule a soma entre
# todos os números impares que são múltiplos de 3,
# que se encontram no intervalo de 1 até 500#

soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c #Acumulador
        cont += 1 #Contador
print('a soma de todos os {} números múltiplos de 3 entre 1 e 500 é: {}'.format(cont,soma))
