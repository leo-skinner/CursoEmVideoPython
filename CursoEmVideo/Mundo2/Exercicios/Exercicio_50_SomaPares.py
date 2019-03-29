#Desenvolva um programa que leia 6 numeros inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere.#
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o número {}: '.format(c)))
    if num%2 == 0:
        cont += 1
        soma += num
        print(num)
print('A soma dos {} valores pares digitados é: {}'.format(cont, soma))
