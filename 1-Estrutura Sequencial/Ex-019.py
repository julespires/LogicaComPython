'''
Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
Autor:Jules do Nascimento Pires
Ex:019
Data:15/01/2025
'''

# Biblioteca
import os
os.system('cls')

# Entrada do preço
preco = float(input('Informe o preço do produto R$:'))

# Calculo
desconto = preco * 5 / 100
novoPreco = preco - desconto

# Mostra o resultado
print('O produto que custava R${:.2f} com 5% de desconto custará R$:{:.2f}'.format(preco, novoPreco))