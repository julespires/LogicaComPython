'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
Autor:Jules do Nascimento Pires
Ex:018
Data:15/01/2026
'''

import os
os.system('cls')

# Entrada dos valores
largura = float(input('Digite a largura:'))
altura = float(input('Digite a altura:'))

# Calculo da área
area = largura * altura

# Mostra a área
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura, altura, area))

# Calcula a quantidade de tinta necessária
tinta = area / 2

# Mostra o resultado
print('Para pintar essa parede, você precisará de  {}l de tinta.'.format(tinta))