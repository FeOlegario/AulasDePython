# Um professor quer sortear um dos sus quatros alunos
# para apagar o quadro. Faça um programa que ajude
# ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
print('Digite o nome dos quatros alunos:')

# usnado o loop for para cirar uma lista 'alunos' e armazenar os nomes.
Alunos = [] 
for i in range(4):
    nome = input(f'Aluno {i+1}: ') # as listas sempre são contadas como [0, 1, 2, 3,..., n], o {i+1} irá transformar em [0+1, 1+1, 2+1, 3+1,...,n+1]
    Alunos.append(nome) # o .append() faz com que os nomes inseridos na variavel "nome" sejam inseridos dentro da lista "Alunos", conforme o professor vá colocando os nomes.


escolhido = random.choice(Alunos)

print(f'O aluno que vai apagar o quadro é {escolhido}')





# Outro metodo de fazer o programa

import random
print('Digite o nome dos quatros alunos:')

a = input('Nome do primeiro aluno: ')
b = input('Nome do segubndo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')

alunos = [a,b,c,d]

escolhido = random.choice(alunos)

print(
    f"""
    O aluno que irá apagar o quadro é o {escolhido}
    """
)