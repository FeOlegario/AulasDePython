Name = input(
    'Digite seu nome: '
             )
print(
    f'É um prazer te conhecer, {Name}!'
)

# Outro modo de fazer isso é usando .format(), ele vai formatar a 
# variável para caber dentro da string. Ex:

Name2 = input(
    'Digite seu nome: '
)
print(
    'É um prazer te conhecer, {}!'.format(Name2)
)
