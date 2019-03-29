#Programa que lê o nome de uma pessoa
#e diz se existe SILVA no nome.

nome = str(input('Digite seu nome: ')).strip()

print('Nome digitado: ', nome.title())
print('Seu nome contém Silva? ', 'SILVA' in nome.upper())
