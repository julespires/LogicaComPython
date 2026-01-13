'''
Escreva um programa que converta uma temperatura digitaa em °C e converta para °F.
Autor:Jules do Nascimento Pires
Ex:014
Data:12/01/2026
'''

import os
os.system('cls')

# Entrada da temperatura
celsius = float(input('Informe a temperatura em °C:'))

# Conversão
farenheit = ((9*celsius)/5)+32

# Mostra o resultado
print('A tempera de {} °C corresponde a {} °F!'.format(celsius, farenheit))