#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

"""""
#Abaixo foi usado apenas forma matematica
cateto_o = float(input('Qual o comprimento do cateto oposto: '))
cateto_a = float(input('Qual o comprimento do cateto adjacente: '))
hipotenusa = (cateto_o ** 2 + cateto_a ** 2) ** (1/2)

print(f'A HIpotenusa vai medir {hipotenusa:.2f}')
"""

"""
#Aqui vai ser usado a importação da classe math
import math
cateto_o = float(input('Qual o comprimento do cateto oposto: '))
cateto_a = float(input('Qual o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_o, cateto_a)
print(f'A hipotesusa vai medir {hipotenusa:.2f}.')

"""
#Aqui vai sair o mesmo resultado usando o from

from math import hypot

cateto_o = float(input('Qual o comprimento do cateto oposto: '))
cateto_a = float(input('Qual o comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_o, cateto_a)
print(f'A hipotesusa vai medir {hipotenusa:.2f}.')
