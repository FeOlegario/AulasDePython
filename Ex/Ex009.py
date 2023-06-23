# Escreva um programa que leia um número inteiro qualquer
# e mostre na tela sua tabuada.

NI = int(input('Digite um número inteiro: '))
print(
    f"""
    A tabuada do número {NI} é:
    """ 
)
for T in range(1,11):
    result = NI * T
    print(
        f"""    {NI} x {T:2} = {result:2}"""
    )