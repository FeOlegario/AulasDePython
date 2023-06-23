# Escreva um programa que converta uma 
# temperatura digitando em graus Celsius 
# e converta para graus Fahrenheit.

Tc = float(input('Informe a temperatura em °c: '))
print(
    f"""
    A temperatura de {Tc}°C corres ponde a {(Tc * 9/5)+32}°F
    e {Tc+273.15}K
    """
)