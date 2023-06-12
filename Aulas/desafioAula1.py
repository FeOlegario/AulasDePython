# Crie um script Python que leia o 
# nome de uma pessoa e mostre uma mensagem
# de boas-vindas de acorddo com o valor digitado

nome = input('Qual o seu nome?')
print ('olá',nome,'!','Prazer em te comhecer!')


# Crie um script Python que leia o 
# dia, o mês e o ano de nascimento 
# de uma pessoa e mostre uma mensagem
# com a data formatada

dia = input('Qual o dia do seu aniversário?')
mes = input('Qual o mês do seu aniversário? Por extenso.')
ano = input('Qual o ano do seu aniversário?')

print(
    'Você nasceu no dia', dia,'de', mes,'de',ano,'. correto?'
)


# Crie um script Python que leia  
# dois números e tente mostrar
# a soma entre eles.

n1 = input ('Escolha um número:')
n2 = input ('Escolha outro número:')
n1_int = int(n1)
n2_int = int(n2)
soma = n1_int + n2_int
print(
    f'A soma de {n1_int} + {n2_int} é:{soma}'
)


# O "imput" faz o usuário criar um string e o "int" transfomar a string para um número inteiro, fazendo assim possível
# a soma entre as duas strings.
# Usar sempre o 'f' no inicio quando a linha for uma função. {} serve para sinalizar uma variável, é preciso usar o 'f' no inicio para funcionar.