'''
Faça um programa que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.
Autor:Jules do Nascimento Pires
Ex:006
Data:23/01/2026
'''

import os
os.system('cls')

# Entrada do preço
preco = float(input('Informe o preço do produto:'))

# Calcula o novo preço com 10% de desconto
novoPreco = preco - (preco * 10/100)

# Mostra o resultado
print('O novo preço com 10% de desconto ficará por:R${:.2f}'.format(novoPreco))