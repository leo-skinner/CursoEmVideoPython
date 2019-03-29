# Crie um algoritmo que leia
# um número e mostre seu dobro,
# triplo e sua raiz quadrada

num = float(input("digite um número: "))

dobro = num * 2
triplo = num * 3
raiz = num**(1/2)

print("O numero digitado foi: {}\nSeu dobro: {}\nSeu triplo {}\nSua Raiz: {:.2f}" .format(num, dobro, triplo, raiz))
