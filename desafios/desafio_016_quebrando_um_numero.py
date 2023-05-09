#Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#Abaixo uma das formas de fazer isso
"""""
import math
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {math.trunc(num)}')

"""""

# Abaixo outra forma de fazer com o mesmo resultado
"""""
from math import trunc
num = float(input('Digite um valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')
"""

# Abaixo outra forma de fazer com o mesmo resultado
num = float(input('Digite o valor: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)} .')

#acima é a forma mais facil mas temos de aprender todas as formas de fazer.