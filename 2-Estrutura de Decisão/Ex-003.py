'''
Faça um programa que receba duas notas, calcule e mostre a média aritmética e a mensagem que se encontra na tabela a seguir:
MÉDIA aritmética                                      mensagem
0,0 ------- 3,0                                               Reprovado
3,0 ------- 7,0                                               Exame
7,0 ------- 10,0                                              Aprovado
Autor:Jules do Nascimento Pires
Data:09/01/2026
'''

import os
os.system('cls')

# Entrada das notas
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))

# Calcula a média
media = (nota1 + nota2) / 2
print('Média aritimética:{}'.format(media))

# Condições
if (media >= 0 and media < 3.0):
    print('Reprovado')

elif (media >= 3.0 and media < 7.0):
    print('Fazer exame!')

elif (media >= 7.0 and media <= 10.0):
    print('Aprovado!')