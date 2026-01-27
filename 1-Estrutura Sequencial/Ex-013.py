'''
Faça um programa que receba o valor do salário mínimo e o valor do salário de um funcionário
calcule e mostre a quantidade de salários mínimos que esse funcionário ganha.
Autor:Jules do Nascimento Pires
Ex:013
Data:26/01/2026
'''

import os
os.system('cls')

salario = float(input('Valor do salário mínino:R$'))
salarioFuncinario = float(input('Salário do funcionário:R$'))

quantidadeSalario = salarioFuncinario / salario

print('Você recebe {:.0f} salários mínimos'.format(quantidadeSalario) )

