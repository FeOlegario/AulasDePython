# Faça um programa que leia o comprimento do cateto
# oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

import math
print('Defina os valores dos catetos de um triangulo retângulo, para achar a hipotenusa')
Co = float(input('Defina o valor do cateto oposto: '))
Ca = float(input('Defina o valor do cateto adjacente: '))
H = math.hypot(Co,Ca)
print(
    f"""
    O triângulo retângulo que possui o cateto oposto de {Co} e o cateto adjacente de {Ca}
    tem a hipotenusa de {H:.2f} 
    """
)