'''
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: A = ((base maior + base menor) * altura) /2
Autor:Jules do Nascimento Pires
Ex:010
Data:23/01/2026
'''

# Biblioteca de sistema
import os
os.system('cls')

# Entrada dos dados
altura = float(input('Altura:'))
baseMaior = float(input('Base maior:'))
baseMenor = float(input('Base menor:'))

# Calcula a área do trapézio
area = ((baseMaior + baseMenor) * altura)/2

# Mostra o resultado
print('Área do trapézio:{}'.format(area))