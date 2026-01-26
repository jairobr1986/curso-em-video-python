# Exercício 75 – Análise de dados em uma Tupla
# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.


a = None
b = None
c = None
d = None

a = int(input("Digite um Número: "))
b = int(input("Digite um Número: "))
c = int(input("Digite um Número: "))
d = int(input("Digite um Número: "))

valor_tupla = ( a, b, c,d)

print(valor_tupla)
print(f'O valor 9 aparece {valor_tupla.count(9)} vezes')
print(f'O valor 3 está na [{valor_tupla.index(3)+1}ª Posição], \nou  na posição: [{valor_tupla.index(3)}], Se começar do contar do zero.')


if a % 2 == 0:
    print(f'De: {valor_tupla} \n[{a}] é par.')
if b % 2 == 0:
    print(f'De: {valor_tupla} \n[{b}] é par.')
if c % 2 == 0:
    print(f'De: {valor_tupla} \n[{c}] é par.')
if d % 2 == 0:
    print(f'De: {valor_tupla} \n[{d}] é par.')
    
