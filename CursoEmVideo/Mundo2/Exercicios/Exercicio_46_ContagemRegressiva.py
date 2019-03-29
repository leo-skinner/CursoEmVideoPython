#Faça um programa que mostre na tela
# uma contagem regressiva para o estouro
# fogos de artifício, indo de 10 a 0, com
# intervalo de 1 segundo.#
import time

print('+-+'*7)
print('contagem regressiva')
print('+-+'*7)
time.sleep(3)
for c in range (10,-1, -1):
    print(c)
    time.sleep(1)
print('Boom!')