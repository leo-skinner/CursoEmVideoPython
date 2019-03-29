algo = input("Digite Algo: ")

print("O tipo primitivo do valor digitado é: ", type(algo))
print("Somente tem espaços? ", algo.isspace())
print("É um número? ", algo.isnumeric())
print("É decimal ?", algo.isdecimal())
print("É Somente maiusculas? ", algo.isupper())
print("É somente minusculas? ", algo.islower())
print("Está Capitalizado? ", algo.istitle())
print("É alfanumerico ?", algo.isalnum())

