'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Autor:Jules do Nascimento Pires
Ex:017
Data:15/01/2026
'''

# Biblioteca
import os
os.system('cls')

# Entrada do número
real = float(input('Quanto dinheiro você tem na carteira?'))

# Conversão 
dolar = real / 3.27

# Mostra o resultado
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))