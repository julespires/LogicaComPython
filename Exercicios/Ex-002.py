'''
Faça um programa que receba três notas, calcule e mostre a média aritmética.
Autor:Jules do Nascimento Pires
Ex:002
Data:06/01/2026
'''

# Entrada das notas
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('Terçeira nota:'))

# Calcula a média aritimética
media = (nota1 + nota2 + nota3) / 3

# Mostra o resultado
print('Média aritimética das notas:{:.2f}'.format(media))