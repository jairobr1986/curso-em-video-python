# Exercício 60 – Cálculo do Fatorial
# Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

# Exemplos práticas repetição
# 5! = 5 x 4 x 3 x 2 x 1 = 120

# from math import factorial
# num = int(input('Digite o número: '))
# fatorial_numero = factorial(num)
# print(fatorial_numero)
# # usando biblioteca acima
# # ======================================

entrada = int(input('Digite o número: '))
num = entrada
contador = 1

while num > 0:
    print(f'{num}', end='')
    print(f' x ' if num > 1 else ' = ', end='')
    contador *= num
    num -= 1
   
print(f'O fatorial de {entrada}, é {contador}')
