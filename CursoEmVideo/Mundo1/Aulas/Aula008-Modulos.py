# import, importa tudo.
# from <biblioteca> import <objeto> limita o import.

# import math -> Importa a biblioteca inteira
# para especificar a importação digite abaixo:

from math import sqrt, ceil, floor

# desta forma, não precisa chamar a classe math.sqrt, apenas sqrt.

num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('a raiz quadrada de {} e {}' .format(num, ceil(raiz)))
#ceil = arredonda para cima
#floor = arredonda para baixo
