'''
Faça um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
Autor:Jules do Nascimento Pires
Ex:007
Data:02/01/2026
'''

# Entrada das notas
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))

# Calculo da média
media = (nota1 + nota2) / 2

# Resultado
print('A média entre {} e {} = {}'.format(nota1, nota2, media))