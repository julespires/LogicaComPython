'''
Faça um programa que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
Autor:Jules do Nascimento Pires
Ex:020
Data:17/01/2026
'''

import os
os.system('cls')

# Entrada do salário atual
salario = float(input('Qual é o salário do Funcionário? R$'))

# Calcula o novo salário
novoSalario = salario + (salario * 15 / 100)

# MOstra o resultado
print('Seu novo salário com 15% de aumento será de R$:{:.2f}'.format(novoSalario))