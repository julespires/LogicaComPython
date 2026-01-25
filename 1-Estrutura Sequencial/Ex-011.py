'''
Faça um programa que calcule e mostre a área de um quadrado. Sabe-se que: A = lado * lado.
Autor:Jules do Nascimento Pires
Ex:011
Data:24/01/2026
'''

# Biblioteca de sistema
import os
os.system('cls')

# Recebe os lados
lado1 = float(input('Lado 1:'))
lado2 = float(input('Lado 2:'))

# Calcula a área
area = lado1 * lado2

# Mostra a área
print('Área do quadrado:{}cm'.format(area))