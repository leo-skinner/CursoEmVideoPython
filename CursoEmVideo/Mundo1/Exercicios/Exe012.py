# Programa que lê um preço e retorna com 5% de desconto.

preco = float(input("Entre o valor da mercadoria: "))

desconto = preco*0.05
valorDesconto = preco-desconto


print("A mercadoria com 5% de desconto fica R${:.2f}. O valor do desconto é de R${:.2f}" .format(valorDesconto,desconto))