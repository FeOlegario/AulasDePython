# Crie um programa que leia um número Real qualquer
# pelo teclado e mostre na tela a sua porção inteira
# Ex:
# digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

# Sem biblioteca

Nr = float(input('Digite um número Real: '))
print(
    f"""
    O número {Nr} tem a parte inteira {int(Nr)}
    """
)

# Com a biblioteca math

import math
N = float(input('Digite um número Real: '))
print(
    f"""
    O número {N} tem a parte inteira {math.trunc(N)}
    """
)