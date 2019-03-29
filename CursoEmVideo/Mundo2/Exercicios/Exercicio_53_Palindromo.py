# Desenvolva um programa que leia uma frase
# e diga se ela é um Palíndromo (frase que você
# lê de traz para frente e mantém o sentido,
# desconsiderando os espaços)
# exempos: Apos a Sopa, A sacada da casa,
# a torre da derrota, o lobo ama o bolo, anotaram a data da maratona.#

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
if junto == inverso:
    print(junto, inverso)
    print('A frase {} é Palíndromo.'.format(frase))
else:
    print(junto, inverso)
    print('A frase {} não é palíndromo.'.format(frase))
