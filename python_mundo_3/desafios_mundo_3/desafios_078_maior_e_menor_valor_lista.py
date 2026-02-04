# Exercício 78 – Maior e Menor valores na Lista
# Exercício Python 078: Faça um programa que leia 5 valores numéricos 
# e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado 
# e as suas respectivas posições na lista.

leitor_numeros = list()

while True:
    try:
        leitor_numeros = list(int(input('Digite o número desejado: ')) for _ in range(1, 6))
        comparador = leitor_numeros
    except ValueError:
        print('Apenas número inteiros são aceitos.')

    if len(leitor_numeros) == 5:
        break

print(leitor_numeros)
maior = max(leitor_numeros)
menor = min(leitor_numeros)

for pos, na_lista in enumerate(leitor_numeros):
    if maior == na_lista:
        print(f'O maior número é [{maior}], e está na posição [{pos}]')

print()
print(f'O maior número é {max(leitor_numeros)}')
print()
print(f'O menor número é {min(leitor_numeros)}')