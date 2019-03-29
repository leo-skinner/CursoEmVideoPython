## Fatiamento de String
frase = 'Curso em Video Python'
print('FATIAMENTO DE STRING')
print('')
print('Print(frase)- Imprime a frase guardada na memória - ', frase)
print('Esta frase ocupa 21 posições na memórica, ou seja, de 0 até 20.')
print('')
print('frase[9]- Exibe somente o caracter na posição 9 da memória - ', frase[9])
print('frase[9:13] - Exibe da posição 9 até a 12, excluindo a 13 - ',frase[9:13])
print('frase[9:21] - exibe da posição 9 até a 20 na memória - ', frase[9:21])
print('frase[9:21:2] - Exibe os caracteres pulando 2 casas - ', frase[9:21:2])
print('frase[:5] - inicia da posição 0 até a 5, excluindo a mesma. - ', frase[:5])
print('frase[15:] - inicia da posição 15 até o final.', frase[15:])
print('frase[9::3 - inicia da posição nove, até o final, pulando 3 casas',frase[9::3])
print('')
print('ANALISE DE STRING')
print(frase)
print('len(frase) - mostra o comprimento da frase', len(frase))
print("frase.count('o') - mostra quantas vezes aparece a letra o - ", frase.count('o'))
print("frase.count('o',0,13) - exibe o numero de letras o entre o espaço de memória selecionado - ", frase.count('o',0,13))
print("frase.find('deo') - Indica a posição inicial de uma string -", frase.find('deo'))
print("frase.find('Android') - Retorna -1 se não encontrar -", frase.find('Android'))
print("'Curso' in frase - Retorna TRUE ou FALSE, se a palavra exitir ou não (Case sensitive) - ",'Curso'in frase)
print('')
print("Transformacao")
print('')
print("frase.replace('Python,'Android') - Substitui uma palavra pela outra (somente na memória) - ", frase.replace('Python','Android' ))
print("frase.upper() - Coloca a frase em maiuscula", frase.upper())
print("frase.lower() - Coloca tudo em minusculas - ", frase.lower())
print("frase.capitalize() - Somente as primeiras maiusculas", frase.capitalize())
print("frase.title() - Capitaliza palavra por palavra - ", frase.title())
print('')
print('')
frase2 = '   Aprenda Python  '
print(frase2)
print("A frase2 possui ",len(frase2), " posições.")
frase2curta = frase2.strip()
print("frase2.strip() - Remove espaços no inicio e final da string - ",frase2curta)
print("Após o strip(), a frase2 possui ",len(frase2curta), " posições.")

# Print com 3 aspas duplas respeita as quebras de linhas.

print("""

Lá no alto daquele cume
Plantei um pé de roseira
O Mato no cume cresce
A rosa no cume cheira.

""")

#Combinações
print('Combinações')
print('')
print(frase)
print("frase.upper().count('0') - Coloca a frase em maiúsculas e conta o numero de letras o - ",frase.upper().count('O'))
print('')
print('')
print("frase.split() - Divide a frase em blocos, criando uma lista - ", frase.split())
print("dividido = frase.split - Variavel recebe a lista.")
dividido = frase.split()
print("dividido[0] - mostra o item na posição 0 - ", dividido[0])
print("dividido[2][3] - indica o item na posição 2 e mostra a letra da posição 3 - ", dividido[2][3])
