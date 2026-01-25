'''
Faça um programa que receba dois números e mostre o menor.
Autor:Jules do Nascimento Pires
Ex:002
Data:24/01/2026
'''

import os
os.system('cls')

num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))

if (num1 > num2):
    print('O número {} é o maior'.format(num1))

elif(num2 > num1):
    print('O número {} é o maior'.format(num2))

else:
    print('Os valores são iguais!')