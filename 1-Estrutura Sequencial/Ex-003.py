'''
Faça um programa que receba três números, calcule e mostre a multiplicação desses números.
Autor:Jules do Nascimento Pires
Ex:003
Data:21/01/2026
'''

import os
os.system('cls')

# Entrada dos dados
num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))
num3 = int(input('Terçeiro valor:'))

# Realiza a multiplicação
mult = num1 * num2 * num3

# Mostra o resultado
print('A multiplicação entre: {} x {} x {} = {}'.format(num1, num2, num3, mult))