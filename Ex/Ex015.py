# Escreva um programa que pergunte a quantidade de Km 
# percorridos por um carro alugado e a quantidade de dias 
# pelos quais ele foi alugado. Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('Coloque os dados a seguir para saber o valor final do aluguel.')
D = float(input('Informe quantos KM foi rodado com o veículo: '))
T = int(input('Informe por quantos dias foi alugado: '))
print(
    f"""
    O total a pagar é de R${T*60 + D*0.15:.2f}
    """
)