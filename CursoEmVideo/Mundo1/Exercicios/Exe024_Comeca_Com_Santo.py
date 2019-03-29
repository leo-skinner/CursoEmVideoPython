#Crie um programa que leia o nome de uma cidade
#e diga se ela começou ou não por Santo.

cidade = str(input('Digite a Cidade: ')).strip() #elimina os espaços. inicio e fim.
print('Cidade digitada: {}'.format(cidade.capitalize())) # Acertar a forma digitada.

#Criar uma lista de palavras, retirando os espaços entre cada uma.
lista = cidade.split()

print('Começa com Santo? ', 'SANTO' in lista[0].upper()) #Verificar em maiúsculas.
