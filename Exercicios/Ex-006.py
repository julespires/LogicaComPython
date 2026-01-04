'''
Faça um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.
Autor:Jules do Nascimento Pires
Ex:006
Data:02/01/2026
'''

# Recebe um número
numero = int(input('Digite um número:'))

# Calculo
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)

# Resultado
print('O dobro de {} vale {}.'.format(numero, dobro))
print('O dobro de {} vale {}.'.format(numero, triplo))
print('O dobro de {} vale {:.2f}.'.format(numero, raiz))