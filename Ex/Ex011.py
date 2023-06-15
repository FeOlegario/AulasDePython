# Faça um programa que leia a largura e altura de uma parede
# em metros, calcule a sua área e a quantidade de tinta neces
# sária para pintá-la, sabendo que cada litro de tinta,pinta 
# uma área de 2m².
A = float(input('Digite a altura da parede em metros: '))
L = float(input('Digite a largura da parede em metros: '))

area = float(A * L)
qt_tinta = float(area/2)

print(
    f"""
    A parede possuí {A}m por {L}m.
    Sua área é {area} m².
    Será necessário {qt_tinta} litros para pintar toda parede.
    """
)
