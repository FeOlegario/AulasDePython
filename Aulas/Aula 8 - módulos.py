# Usando a biblioteca math
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)

print(f'A raiz de {num} é {raiz:.2f}')
print(f'A raiz de {num} é {math.ceil(raiz)}')
# usando o math.ceil() fará que o número seja arredondado para cima


# Usando a biblioteca math porém pedindo as funções especificas
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)

print(f'A raiz de {num} é {raiz:.2f}')
print(f'A raiz de {num} é {floor(raiz)}')
# Assim, não é necessário usar o math.função(), 
# pois quando especificamos a função, como foi na 
# primeira linha, que pedimos a fuinção sqrt (raiz quadrada) 
# e a função floor (arredondamento para baixo), 
# basta colocar na formatação a função que será utilizada, 
# como nas linhas 4 e 7