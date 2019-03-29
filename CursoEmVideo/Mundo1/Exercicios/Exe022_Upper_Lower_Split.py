#Crie programa que leia o nome completo e mostre:
#- O nome com Uppercase
#- O nome com Lowercase
#- Quantas letras ao no total, sem considerar espaços
#- Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip() #para eliminar possíveis espaços no início e final da string.

print('Seu nome em uppercase: ', nome.upper())
print('Seu nome em lowercase: ', nome.lower())
# usando replace...
print('1- Número de letras de seu nome completo: ', len(nome.replace(' ', '')))

# usando subtração de espaços
print('2- Número de letras de seu nome completo: ', len(nome) - nome.count(' '))

letras = nome.split()

print('Seu primeiro nome é {} e tem: {} letras' .format(letras[0] ,len(letras[0]), 'letras.'))

