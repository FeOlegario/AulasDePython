# Faça um programa que leia um ângulo e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo

import math
print('Digite um ângulo para saber seu seno, cosseno e tangente')

a = float(input('Digite o valor do ângulo: '))
ar = math.radians(a)

print(
    f"""
    O angulo de {a}° tem:
    Seno = {math.sin(ar):.2f}
    Cosseno = {math.cos(ar):.2f}
    Tangente = {math.tan(ar):.2f}
    """
)
