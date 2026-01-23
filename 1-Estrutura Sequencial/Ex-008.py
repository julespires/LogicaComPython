'''
Faça um programa que receba o peso de uma pessoa, calcule e mostre:
a) o novo peso, se a pessoa engordar 15% sobre o peso digitado;
b) o novo peso, se a pessoa emagrecer 20% sobre o peso digitado.
Autor:Jules do Nascimento Pires
Ex:008
Data:23/01/2026
'''

import os
os.system('cls')

# Entrada do peso
peso = float(input('Informe o seu peso:'))

# Calcula os pesos
peso15 = peso + (peso * 15 / 100)
peso20 = peso + (peso * 20 / 100)

# Mostra o resultado

print('-'*50)
print('Atualmente você pesoa:{}\nse você engordar 15%, seu novo peso será de:{:.2f}\nmas se engordar 20% seu novo peso será de:{:.2f}'.format(peso, peso15, peso20))
print('-'*50)
