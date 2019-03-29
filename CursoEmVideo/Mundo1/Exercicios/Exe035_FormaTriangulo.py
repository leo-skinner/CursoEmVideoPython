# Três retas podem formar um triângulo?

print('-='*15)
print('Analisador de Triângulos')
print('=-'*15)

r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))

# Somente forma triângulo se a soma de dois lados for maior que o segmento.

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os três seguimentos formam um triângulo.')
else:
    print('As retas não formam um triângulo.')
