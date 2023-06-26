# Faça um programa que leia de 0 a 9999 e mostre na tela
# cada um dos digitos separados.

# Ex:
# Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

num = int(input('Digite um número de 0 a 9999: '))

print(
    f"""
    Unidade: {num // 1 % 10}
    Dezena: {num // 10 % 10}
    Centena: {num // 100 % 10}
    Milhar: {num // 1000 % 10}
    """
)