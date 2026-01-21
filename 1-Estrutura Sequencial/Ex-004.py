'''
Faça um programa que receba dois números, calcule e mostre a divisão do primeiro número pelo segundo. Sabe-se que o segundo número não pode ser zero, portanto, não é necessário se preocupar com validações.
Autor:Jules do Nascimento Pires
Ex:004
Data:21/01/2026
'''

import os
os.system('cls')

num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))

div = num1 / num2

print('A divisão entre {} / {} = {:.0f}'.format(num1, num2, div))