'''
Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
Autor:Jules do Nascimento Pires
Ex:012
Data:03/01/2026
'''

import os
os.system('cls')

# Entrada do preço
preco = float(input('Informe o preço do produto:'))

# Calcula o novo preço
novoPreco = preco - (preco * 5 / 100)

# Mostra o resultado
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novoPreco))
