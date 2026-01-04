'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
Autor:Jules do Nascimento Pires
Ex:004
Data:01/01/2026
'''

# Recebe algo na tela
a = input('Digite algo:')

# Mostra os tipos
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada? ', a.istitle())