# Crie um programa que converta reais em dolar (1 dolar = R$3,27).

reais = float(input("Quantos Reais você tem? "))
dolar = reais/3.27
print("Com seus míseros R${:.2f}, você compra US${:.2f}" .format(reais,dolar))

if dolar>=10.0:
    print("Você está rico!")

else:
    print("Seu pobretão!")
