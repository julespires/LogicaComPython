'''
Faça um programa que converta uma temperatura digitada em °C e converta para °F.
Autor:Jules do Nascimento Pires
Ex:021
Data:17/01/2025
'''

import os 
os.system('cls')

# Entrada da temperatura em Celsius
c = float(input('Informa a temperatura em °C:'))

# Calculo
f = ((9 *c) / 5) + 32

# Mostra a temperatura em Farenheit
print('A temperatura de {}°C corresponde a {}°F!'.format(c,f))