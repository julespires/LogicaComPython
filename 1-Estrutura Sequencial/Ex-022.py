'''
Faça um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de
dia pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
e R$0,15 por Km rodado.
Autor:Jules do Nascimento Pires
Ex:022
Data:17/01/2026
'''
import os
os.system('cls')

# Entradas dos dados
dias = int(input('Quantos dias alugadors?'))
km = float(input('Quantos km rodados?'))

# Calculo
pago = (dias * 60) + (km * 0.15)

# Resultado
print('O total a pagar é de R$:{:.2f}'.format(pago))