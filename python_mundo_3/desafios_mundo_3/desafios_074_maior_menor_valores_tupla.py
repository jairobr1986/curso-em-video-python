# Exercício 74 – Maior e menor valores em Tupla
# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios 
# e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados 
# e também indique o menor e o maior valor que estão na tupla.

# Pensamento abaixo
# criar tupla -> usar variavel

# gerar 5 numeros aleatorios -> usar rando
# colocar na tupla -> números gerados colocar na tupla
# mostrar numeros gerados -> usar print
# mostrar menor e maior valor -> usar condicional if depois o print

from random import randint

valores = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))

for contador_de_tupla in valores:
    print(f'{contador_de_tupla}',end=' ')
print(f'O maior valor é {max(valores)} e o menor valor é {min(valores)}')

