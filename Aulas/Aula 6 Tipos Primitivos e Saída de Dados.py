n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: ' ))
s = n1 + n2
print('A soma vale:', s)

# testando classes

# STR
n3 = input('Digite um valor: ')
print(type(n3))

# INT
n3 = int(input('Digite um valor: '))
print(type(n3))


#DESAFIO um print escrito: "a soma entre x e y vale z"
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
# print(f'A soma de {x} e {y} vale {x + y}')
print('A soma entre {} e {} vale {}'.format(x,y,x+y)) # usar agora mais o .format() para o print
