# Desenvolva um programa que leia
# as duas notas de um aluno e retorne sua média.

nota1 = float(input("Insira a nota da prova 1: "))
nota2 = float(input("Insira a nota da prova 2> "))

media = (nota1+nota2)/2

if media >= 5:

    print("Sua média é {:.2f}. Parabéns! Você passou" .format(media))

else:

    print("Sua média é {:.2f}. Você está em recuoeração" .format(media))
