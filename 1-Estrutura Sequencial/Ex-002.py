'''
Faça um programa que receba dois números, calcule e mostre a subtração do primeiro número pelo segundo.
Autor:Jules do Nascimento Pires
Ex:002
Data:21/01/2026
'''

import os
os.system('cls')

# Entrada dos valores
num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))

# Realiza a subtração
subtracao = num1 - num2

# Mostra o resultado
print('A subtração entre {} - {} = {}'.format(num1, num2, subtracao))