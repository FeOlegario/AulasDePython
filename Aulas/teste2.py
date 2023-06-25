# import random

# lista = [1, 2, 3, 4]

# # print(f'lista original {lista}')

# random.shuffle(lista)
# print(f'lista embaralhada {lista}')

palavra = input('Digite um palavra: ')
vogais = ['a', 'e', 'i', 'o', 'u']
contador = 0 

for i, letra in enumerate(palavra, start=1):
    if letra.lower() in vogais:
        contador += 1
print(f'A palvra {palavra} possui {contador} vogais')