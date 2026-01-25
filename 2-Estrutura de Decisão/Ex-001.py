'''
Faça um programa que receba quatro notas de um aluno, calcule e mostre a média aritmética das notas e a mensagem de aprovado ou reprovado, considerando para aprovação média 7
Autor:Jules do Nascimento Pires
Ex:001
Data:24/01/2026
'''

import os
os.system('cls')

nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
nota3 = float(input('Terçeira nota:'))
nota4 = float(input('Quarta nota:'))

media = (nota1 + nota2 + nota3 + nota4) / 4

print('Média aritimética:{:.2f}'.format(media))

if (media >= 7.0):
    print('Aprovado!')

else:
    print('Reprovado!')