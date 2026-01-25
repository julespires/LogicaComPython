'''
Faça um programa que calcule e mostre a área de um losango. Sabe-se que: A = (diagonal maior * diagonal menor) /2.
Autor:Jules do Nascimento Pires
Ex:012
Data:24/01/2026
'''

# Biblioteca de sistema
import os
os.system('cls')

# Entrada das diagonais
diagonalMaior = float(input('Diagonal maior:'))
diagonalMenor = float(input('Diagonal menor:'))

# Calculo da área
area = (diagonalMaior * diagonalMenor)/2

# Mostra o resultado
print('Área do losangolo:{}cm'.format(area))