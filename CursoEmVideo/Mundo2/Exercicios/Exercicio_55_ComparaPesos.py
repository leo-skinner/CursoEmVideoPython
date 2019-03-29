#Faca um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lido.#
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o {}o peso: '.format(p)))
    if p == 1: #Se for a primeira pessoa, os pesos são iguais.
        maior = peso
        menor = peso
    else: #Se passar para a segunda pessoa, então faz as comparações e guarda nas respectivas variáveis.
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso digitado foi de {}Kg.'.format(maior))
print('O menor peso digitado foi de {}Kg.'.format(menor))




