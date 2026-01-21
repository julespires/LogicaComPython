'''
Faça um programa que receba duas notas, calcule e mostre a média ponderada dessas notas, considerando peso 2 para a primeira e peso 3 para a segunda.
Autor:Jules do Nascimento Pires
Ex:005
Data:21/01/2026
'''

import os
os.system('cls')

# Entrada das notas
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))

# calcula a média
media = (nota1 + nota2) / 2

# Mostra o resultado
print('A média aritimética entre a nota {} e {} = {}'.format(nota1, nota2, media))