# Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.
P = float(input('Digite o preço do produto: '))
print(
    f"""
    O produto está com desconto de 5%, saindo por R${(P - (P * 0.05)):.2f}
    """
)
