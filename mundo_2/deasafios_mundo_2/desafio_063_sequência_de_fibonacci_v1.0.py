# Exercício 63 – Sequência de Fibonacci v1.0
# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e 
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# A sequencia de Fibonacci é o primeiro número mais o segundo numero
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print(f"{' Sequência de Fibonacci v1.0 ' :=^35}")

n = int(input('Quantos números você quer mostrar: '))

t1 = 0
t2 = 1

print('-='*21)
print(f'{t1} -> {t2}', end=' ')
contador = 3

while contador <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    contador += 1
print('\nfim'.upper())