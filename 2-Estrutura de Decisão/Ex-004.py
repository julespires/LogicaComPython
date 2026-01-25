'''
Faça um programa que receba três números e mostre o maior.
'''

import os
os.system('cls')

num1 = int(input('Primeiro número:'))
num2 = int(input('Segundo número:'))
num3 = int(input('Terçeiro número:'))

maior = max (num1, num2, num3)

print('O maior valor é o número:{}'.format(maior))