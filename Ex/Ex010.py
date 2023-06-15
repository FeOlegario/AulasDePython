# crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dolares ela pode comprar
# considere
#US$ 1.00= R$3.27

real = float(input('Digite quantos Reais você tem para saber quantos dolares pode comprar: '))
dolar = 3.27
print(
    f'Com R${real:,.2f}, você pode comprar ${real/dolar:,.2f} dolares'
)