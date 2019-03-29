# 3 Retas formam um triangulo.
# - Equilátero = todos os lados iguais
# - Isóceles = dois lados iguais
# - Escaleno = todos os lados diferentes.

print('-='*15)
print('Analisador de Triangulos II')
print('-='*15)

r1 = float(input('Reta 1 em cm:'))
r2 = float(input('Reta 2 em cm:'))
r3 = float(input('Reta 3 em cm:'))

# Somente forma triângulo se a soma de dois lados for maior que o segmento.

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os três seguimentos formam um triângulo.')
else:
    print('As retas não formam um triângulo.')
    exit()


# Teste do tipo de triângulo

if r1 == r2 and r1 == r3 and r2 == r3:
    print('Este triangulo é equilatero.')

elif r1 != r2 and r1 != r3 and r2 != r3:
    print('Estre triangulo é Escaleno')

else:
    print('Este triangulo é Isoceles')
