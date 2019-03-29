#Refaça o exercicio 9 mostrando a tabuada de um número
# que o usuário escolher, so que agora utilizando o laço FOR#
print('-=-'*3)
print('Tabuada')
print('-=-'*3)
num = int(input('Digite um número para gerar a tabuada: '))
for c in range(1,11):
    print('{} x {} = {}'.format(num,c,num*c))
