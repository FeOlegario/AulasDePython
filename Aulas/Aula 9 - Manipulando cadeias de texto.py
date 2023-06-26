
# Fatiamento

frase = 'Curso em Video Python'
fespaço = '   Aprendendo Python  '

print(frase) # Desse modo ele irá fazer o print da variavel frase.
print(frase[9]) # Desse modo ele fará o print apenas do indice 9 da variavel frase, ou seja 'V'.
print(frase[9:20]) # Desse modo será o print do indicie 9 ('V') até o 19 ('o'), pois o ultimo sempre será n-1, que aparecerá no print.
print(frase[9:21]) # Assim ele contará o indicie 20 ('n').
print(frase[9:21:2]) # Agora ele fará do incie 9 até o 20, porém pulando de 2 em 2, ou seja, ele retornará ('V''d''o''P''t''o').
print(frase[:5]) # Assim sem especificar onde ele vai começar, ele contará desde o indice 0.
print(frase[15:]) # Assim ele fará do indice 15 até o final da string.
print(frase[9::3])# Ele começa no indice 9, vai até o final só que pulando de 3 em 3. ('v''e''P''h').

# Analise

print(len(frase)) # O len() conta quantios caracteres tem na string.
print(frase.count('o')) # O count() irá fazer uma contagem de quantas vezes o 'o' aparece na string interia.
print(frase.count('o',0,13)) # Assim ele fará a contagem de 'o' no intervalo de 0 a 12 (pois sempre o ultimo é n-1).
print(frase.find('deo')) # O find() irá procura na string onde COMEÇA, como no exemplo, onde começou o 'deo' que é na posição 11.
print('Curso' in frase) # Usando o operador 'in' ele retona True ou False, para valores que tenham ou não dentro da sting

# Transformação

print(frase.replace('Python','Oloco')) # o replace(x,y) transforma um elemento 'X' da string em 'Y', mas sem alterar a variável..
print(frase.upper()) # Transforma de minúsculo e transfoma em maiúsculo.
print(frase.lower()) # Transforma de maiúsculo para minúsculo.
print(frase.capitalize()) # Transforma tudo para minusculo, mas mantendo a primeira em maiúsculo: EXEMPLO DE Como é -> Exemplo de como é
print(frase.title()) # o title() tranforma a primeira letra de cada palavra em maiúsculo: exemplo de como é -> Exemplo De Como É
print(fespaço.strip()) # o strip() remove espaços desnecessários no inicio e no fim da frase. Imagina que "_" seja um espaço, então: '_''_''Teste''_''Aqui''_''_' ->'Teste''_''Aqui'
print(fespaço.rstrip()) # De forma semelhante ao anterior, só que por adicionar o 'r' antes, ele remove somente os espaços a direita
print(fespaço.lstrip()) # igual ao anterior, porém retirando somente a esquerda agora, por conta do 'l'

# Divisão

print(frase.split()) # O split() faz uma lista de dividindo a string em substrings, sem considerar os espaços. Ex: ['Curso', 'em', 'Video', 'Python']
# e cada "bloco" corresponde a um indeice dentro da lista, exemplo: 'Curso' == 0, 'em' == 1. E cara string tem um novo indice, exemplo: 'Curso' -> C == 0, u == 1, r == 2 ; 'em' -> e == 0, m == 1.
# dentro do split() podemos usar:
print(frase.split(sep='em')) # o sep=, ele remove uma string da lista.
print(frase.split(maxsplit=2)) # o maxsplit=, irá definir quantas fatias dentro da lista teremos, exemplo ['Curso', 'em', 'Video Python'], no caso foram 3, pois conta 0,1,2
# podendo juntar as duas especificações
print(frase.split(sep='Video',maxsplit=1)) # Assim retirando a string 'Video' e fazendo uma lsita com 2 ideices: ['Curso em ', ' Python']

# junção

print('-'.join(frase.split())) # O .join() é usado para junção, sendo o '-' oq irá fazer o papel do espaço ex: Curso-em-Video-Python. Note que usei o split() para fazer uma lista de substrings da variavel frase
# se o join foir usado em uma variavel, ele adiciona '-' entre os indices.
print('-'.join(frase)) # ex: C-u-r-s-o- -e-m- -V-i-d-e-o- -P-y-t-h-o-n 
