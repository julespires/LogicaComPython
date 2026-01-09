'''
Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu salário final.
Autor:Jules do Nascimento Pires
Ex:013
Data:09/01/2026
'''

import os
os.system('cls')

# Entrada dos valores
salario = float(input('Salário R$:'))
vendas = float(input('Valor das vendas R$:'))

# Cálculo
comissao = salario * 4 / 100
salarioFinal = salario + comissao

# Resultado
print('Valor da comissão R${} \nSalário final:R${}\n'.format(comissao, salarioFinal))
