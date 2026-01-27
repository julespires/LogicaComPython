'''
Faça um programa que calcule e mostre a tabuada de um número digitado pelo usuário.
Exemplo: Digite um número: 5
5 x 0 = 0                   5 x 5 = 25
5 x 1 = 5                   5 x 6 = 30
5 x 2 = 10                  5 x 7 = 35
5 x 3 = 15                  5 x 8 = 40
Autor:Jules do Nascimento Pires
Ex:014
'''

import os
os.system('cls')

# Entrada do número databuada
numero = int(input('Digite um número desejado:'))

# Mostra a tabuada
print('{} x {} = {}'.format(numero, 1, numero*1))
print('{} x {} = {}'.format(numero, 2, numero*2))
print('{} x {} = {}'.format(numero, 3, numero*3))
print('{} x {} = {}'.format(numero, 4, numero*4))
print('{} x {} = {}'.format(numero, 5, numero*5))
print('{} x {} = {}'.format(numero, 6, numero*6))
print('{} x {} = {}'.format(numero, 7, numero*7))
print('{} x {} = {}'.format(numero, 8, numero*8))
print('{} x {} = {}'.format(numero, 9, numero*9))
print('{} x {} = {}'.format(numero, 10, numero*10))
