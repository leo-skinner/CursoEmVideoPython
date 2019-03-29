#Crie um programa que mostre na tela
# todos os números pares que estão no
# intervalo entre 1 a 50#
from time import sleep
#criada por mim (opção mais econômica).
for c in range(2,52,2):
    print(c)
print('------------| Fim |-------------')
sleep(2)
print('outras soluções')
sleep(1)

for c in range(1,51): #Maior consumo de memória. Para cada ponto que aparece é uma iteração feita.
    print('.', end=' ')
    if c%2 == 0:
        print(c, end=' ')
print('fim.')