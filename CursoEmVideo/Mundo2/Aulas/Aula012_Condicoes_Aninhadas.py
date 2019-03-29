# Condições Aninhadas
#
# IF somente possui dois caminhos...
# Para tratar mais de duas opções, devemos usar a estrutura IF-ELIF-ELSE.
# - Pode existir IF sem ELSE
# - Pode existir 1 ou mais ELIF dentro de um IF
# - ELSE pode ou não existir quando somente houver IF
# - ELSE é sempre obrigatório quanto houver 1 ou mais ELIF

nome = str(input("Qual o seu nome ? "))

if nome == 'Augusto':
    print('{} é o nome do meu filho!'.format(nome))

elif nome == 'Isabel':
    print('{} é o nome de minha filha!'.format(nome))

elif nome == 'Pedro' or 'Paulo' or 'Lucas' or 'Matheus' or 'Thiago':
    print('{} é o nome de um dos apóstilos de Jesus'.format(nome))

else:
    print('Seu nome é muito comum')

print('Tenha um bom dia {}'.format(nome))



