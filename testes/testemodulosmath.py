import math
n = int(input('Digite um número: '))
raiz = math.sqrt(n)
print('A raíz de {} é igual a {}.'.format(n, math.ceil(raiz)))
# math.ceil(raiz) importa a função ceil da biblioteca math
# Também posso usar from math import ceil para importar apenas a função ceil, ou a função sqrt, por ex.
