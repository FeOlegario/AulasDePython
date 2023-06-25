# O mesmo professor do desafio anterior quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatros alunos
# e mostre a ordem sorteda.

import random
print('coloque o nome dos alunos para sortear:')

alunos = []
for i in range(4):
    nome = input(f'aluno {i+1}: ')
    alunos.append(nome)

random.shuffle(alunos)

print('A dordem de apresentação é:')
for i, aluno in enumerate(alunos, start=1): # função enumarete() serve para numerar no caso a lista alunos, começando pelo número 1. a sintax é enumerate(oq quer numera, start=x) onde x é um número
    print(f'Trabalho {i}: {aluno}')