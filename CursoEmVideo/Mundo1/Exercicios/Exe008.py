# Escreva um programa que leia um valor em metros
# e retorne em cm e mm.

metros = float(input("Insira o valor em metros: "))

cm = metros*100
mm = metros*1000

print("{:.2f} metros\n{:.2f} centímetros\n{:.2f} milímetros" .format(metros, cm, mm))
