# Crie um programsa que leia duas notas de um aluno e calcule
# sua média, mostrando uma mensagem final, de acordo com a meta:
# - Media < 5 = reprovado
# - Media entre 5 e 6.9 = recuperação
# - Media maior ou igual a 7 = aprovado.#

notaA=float(input('Nota da prova A: '))
notaB=float(input('Nota da prova B: '))

media = (notaA+notaB)/2

if media <= 5.0:
    print('Reprovado. Sua média é ',media)
elif media > 5.0 and media < 6.9:
    print('Recuperação Sua média é ',media)
else:
    print('Aprovado Sua média é ',media)
