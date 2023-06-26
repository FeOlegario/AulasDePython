# Crie um programa que leia o nome completo de uma epssoa e mostre:
# - O nome com todas as letras maiúculas.
# - O nome com todas as letras minúscuylas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

name = input('Digite o seu nome completo: ').strip()
name_s = name.split()
print(
    f"""
    {name.upper()}
    {name.lower()}
    {len(name.replace(' ',''))}
    Seu primeiro nome é {name_s[0]} e tem {len(name_s[0])} letras
    """
)
  