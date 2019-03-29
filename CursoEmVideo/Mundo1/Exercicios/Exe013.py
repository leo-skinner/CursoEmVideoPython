# Programa que lê salário e retorna com 15% de aumento.

salario = float(input("Enrre com o valor do Salario: "))
aumento = salario*0.15
total = salario+aumento

print("Você terá 15% de aumento, que equivale a R${:.2f}\nSeu salario passará para R${:.2f}" .format(aumento, total))
