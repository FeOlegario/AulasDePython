# Desenvolva um programa que leia as duas notas de um aluno, calcule e msotre a 
# média

n1 = int(input('Digite a primeira nota do aluno ciclano: '))
n2 = int(input('Digite a segunda nota: '))
print(
    f"""
    Cilcano obteve a primeira nota: {n1}
    A segunda nota foi {n2}
    E sua média ficou em {(n1+n2)/2}
    """
)