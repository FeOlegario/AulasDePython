# Faça um programa que leia algo pelo teclado e mostre na tela
# o seu tipo primitivo e todas as informações possíveis sobre ela.
a1 = input('Digite algum coisa: ')
# print('A variável a1 é: ', type(a1), '\n'
#     'Elá é uma letra: ', a1.isalpha(),'\n'
#     'Ela é um número: ', a1.isnumeric(), '\n'
#     'Ela é alpha númerico: ', a1.isalnum()
# )
print('A variavel a1 é {}\n'\
      'Ela é um número: {}\n'\
      'Ela é uma letra: {}\n'\
      'Ela é alpha númerico: {}'.format(type(a1), a1.isnumeric(), a1.isalpha(), a1.isalnum())
      )