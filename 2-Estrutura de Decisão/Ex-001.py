'''
Faça um programa que receba dois valores e mostre o maior deles.
Autor:Jules do Nascimento Pires
Ex-001
Data:08/01/2026
'''''

import os
os.system('cls')

num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))

if num1 > num2:
    print('O número {} é maior!'.format(num1))

else:
    print('O número {} é o maior'.format(num2))