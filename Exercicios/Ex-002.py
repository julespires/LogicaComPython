'''
Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas.
Autor:Jules do Nascimento Pires
Ex:002
Data:06/01/2026
'''

import os
os.system('cls')

# Entrada do nome
nome = str(input('Qual é o seu nome'))

print('Olá {}, é um prazer te conhecer!'.format(nome))