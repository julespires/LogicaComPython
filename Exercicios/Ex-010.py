'''
Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Autor:Jules do Nascimento Pires
Ex:010
Data:02/01/2026
'''

# Entrada do valor em reais
real = float(input('Quanto dinheiro você tem na carteira? R$'))

#Converte para dolar
dolar = real / 3.27

# Mostra o resultado
print('Com R${} você pode comprar US${:.2f}'.format(real, dolar))