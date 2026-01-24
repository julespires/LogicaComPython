'''
Faça um programa que receba o peso de uma pessoa em quilos, calcule e mostre esse peso em gramas.
Autor:Jules do Nascimento Pires
Ex:009
Data:23/01/2026
'''

import os
os.system('cls')

# Entrada do peso
peso = float(input('Informe o seu peso:'))

# Conversão em gramas
gramas = peso * 1000

# Mostra o resultado
print('O seu peso de {}kl em gramas é:{}gm'.format(peso,gramas))