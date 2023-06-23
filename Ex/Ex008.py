# Escreva um programa que leia um valor em metros e 
# o exiba convertido em centimetros e milimetros
# Colocar as conversões em km hm dam m dm cm mm

v1 = float(input('Digite um valor em metros: '))
print(
    f"""
    Em quilometro é: {v1/1000} km
    Em hectómetro é: {v1/100} hm
    Em decâmetro é: {v1/10} dam
    O valor escolhido em metros foi: {v1} m
    Em decímetros é: {v1*10:.0f} dm 
    Em centímetros é: {v1*100:.0f} cm
    Em milímetros é: {v1*1000:.0f} mm
    """
)