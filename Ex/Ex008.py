# Escreva um programa que leia um valor em metros e 
# o exiba convertido em centimetros e milimetros

v1 = float(input('Digite um valor em metros: '))
print(
    f"""
    O valor escolhido em metros foi: {v1} m
    E sua conversão para centímetros é: {v1*100} cm
    Sua conversão apra milímetros é: {v1*1000} mm
    """
)