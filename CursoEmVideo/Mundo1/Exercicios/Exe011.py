# Programa que lê LxA de uma parede,
# calcule a área e a quantidade de tinta usada.
# 1 L de tinta pintam 2m^2

largura = float(input("Entre com a largura: "))
altura = float(input("Entre com a altura: "))

area = largura * altura
tinta = area//2

print("Sua parede possui {:.2f}m².\nVocê precisará de {} lata(s)" .format(area,tinta))
