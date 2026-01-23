'''
Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faça um programa que receba o salário fixo do funcionário e o valor de suas vendas, calcule e mostre a comissão e seu salário final.
Autor:Jules do Nascimento Pires
Ex:007
Data:23/01/2026
'''

# Biblioteca de Sistema
import os
os.system('cls')

# Recebe o valor do salário e das vendas
salario = float(input('Informe o salário R$:'))
vendas = float(input('Informe o valor das vendas'))

# Limpa o prompt
os.system('cls')

# Calcula a comissão e o novo salário
comissao = vendas * 4 / 100
novoSalario = salario + comissao

# Mostra o resultado
print('*' * 45)
print('O Funcionário tem um salário de R$:{}\nsua comissão é de R$:{}\nseu novos salário será de R${}'.format(salario, comissao, novoSalario))
print('*' * 45)