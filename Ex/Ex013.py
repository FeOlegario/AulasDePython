# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de almento.
P = float(input('Digite o seu salário: '))
print(
    f"""
   Parabéns, você recebeu 15% de aumento no seu salário!
    A gora seu salário será de R${(P + (P * 0.15)):.2f}
    """
)
