'''
Faça um programa que receba dois números e execute as operações listadas a seguir, de acordo com a escolha do usuário.
Escolha do usuário                                 Operação
1                                     Média entre os números digitados
2                                     Diferença do maior pelo menor
3                                     Produto entre os números digitados
4                                     Divisão do primeiro pelo segundo
Autor:Jules do Nascimento Pires
Data:09/01/2026
'''
# Limpa a saída
import os
os.system('cls')

num1 = float(input('Primeiro valor:'))
num2 = float(input('Segundo valor:'))

op = int(input('Escolha uma opção a seguir: \n1-Média \n2-Diferença \n3-Produto \n4-Divisão \nOpção:'))

# Limpa a saída
os.system('cls')

# Condições
if (op == 1):

    media = (num1 + num2) / 2
    print('Média entre os números digitados:{}'.format(media))

elif (op == 2):
     dif = num1 - num2
     print('Diferença:{}'.format(dif))

elif (op == 3):
     produto = (num1 * num2)
     print('Produto:{}'.format(produto))

elif (op == 4):
     div = num1 / num2
     print('Divisão:{}'.format(div))
     
else:
     print('Operação inexistente!')