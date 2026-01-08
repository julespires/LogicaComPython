'''
Faça um programa que a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
Autor:Jules do Nascimento Pires
Ex:011
Data:03-01-2026
'''
import os
os.system('cls')

# Entrada dos dados
largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))

# Calcula a área
area = largura * altura

# Mostra o resultado
print('Sua parede tem uma dimensão de {}x{} e sua área é de {}m²'.format(largura,altura,area))

# Calcula a quantidade de tinta necessára
tinta = area / 2

# Mostra o resultado
print('Para pintar essa área será necessário:{}L de tinta'.format(tinta))