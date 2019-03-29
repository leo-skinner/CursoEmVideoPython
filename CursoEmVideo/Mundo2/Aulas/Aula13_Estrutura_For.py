# Estruturas de repetição
#
# Estrutura de Laço ou iteração = FOR é uma estrutura de laço ou eternamente ou até chegar a um número definido.
# No Python é chamado laço com variável de controle.
#
# Exemplo:
#
# laço c no intervalo (1 a 10)
#   passo
# pega
#

for c in range(1,10):
    print('passo')

print('pega')
print('---'*20)
# Exemplo 2:
# Um personagem X tem que andar e pular em uma plataforma e pegar uma maça (m).
#
# X           (m)
# __  __  __ ___
#
# O Algoritimo fica:
# Passo-Pula, Passo-pula, Passo-pula, passo-pega
# em pyton:
for c in range (0,3):
    print('passo')
    print('pula')
print('passo')
print('pega')
print('---'*20)
# Estrutura Aninhada.
# Um personagem X tem que andar e pular em uma plataforma e pegar uma maça (m). Agora tem uma moeda em uma das plataformas.
# #
# # X    $      (m)
# # __  __  __ ___#
moeda = bool(True)

for c in range(0,3):
    if moeda == True:
        print('pega moeda')

    print('passo')
    print('pula')
print('passo')
print('pega')
print('---'*20)

# Exemplos da aula:

for c in range(1,6): # Não considera o último número.
    print('oi')
    print(c)
print('fim')
print('---'*20)
# Iteração regressiva

for c in range(6,0, -1):
    print(c)
print('---'*20)

# Iteração de 0 a 7, pulando de 2 em 2.

for c in range(0,7,2):
    print(c)
print('fim')
print('---'*20)

#Interagindo com o laço:
n = int(input('Digite um número: '))
for c in range(0, n+1): #n+1 é para chegar ao número digitado.
    print(c)
print('fim')
print('---'*20)

# Outro exemplo:
i = int(input('inicio: '))
f = int(input('fim: '))
p = int(input('passo: '))

for c in range(i,f+1,p):
    print(c)
print('fim')
print('---'*20)

# Incrementando dados com laço#
soma = 0
for c in range(0,3):
    num = int(input('Digite um número: '))
    soma += num
print('O resultado da soma dos números é: {}'.format(soma))
print('fim')
print('---'*20)
##
