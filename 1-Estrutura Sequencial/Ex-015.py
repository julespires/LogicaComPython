'''
Faça um programa que leia um valor rem metros e o exiba convertido em centímetros e milímetros
Autor:Jules do Nascimento Pires
Ex:015
Data:14/01/2025
'''

import os
os.system('cls')

# Entrada da medida
medida = float(input('Digite uma distância em metros:'))

# Conversão
cm = medida * 100
mm = medida * 1000

# Mostra o resultado
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))