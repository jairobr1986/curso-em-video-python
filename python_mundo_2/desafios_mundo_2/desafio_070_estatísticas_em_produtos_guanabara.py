# Exercício 70 – Estatísticas em produtos
# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. 

# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print()
print(f"{' Exercício 70 – Estatísticas em produtos ':=^70}".upper())
print()

contador = menor_preco = mais_1000 = total_gasto = 0
produto_barato = ' '

while True:

    name_product = str(input('Qual o nome do produto: '.upper()))
    price = float(input('Qual o preço do produto: R$ '))
    total_gasto += price
    contador += 1

    if price > 1000:
        mais_1000 += 1
    
    if contador == 1:
        menor_preco = price
    if price < menor_preco:
        menor_preco = price
        produto_barato = name_product
        
    parar = ' '
    while not parar in 'SN':
        parar = str(input('Quer continuar S/N: '.upper())).strip().upper()[0]
        if not parar in 'SN':
            print('Comando Invalido!')
            continue

    
    if parar == 'N':
        break

print('Programa Finalizado!'.upper())
print()
print('A) qual é o total gasto na compra.')
print(f'O total gasto foi R$[{total_gasto}]'.title())
print()
print('B) quantos produtos custam mais de R$1000.')
print(f'[{mais_1000}] produtos, mais de 1000R$.'.title())
print()
print('C) qual é o nome do produto mais barato.')
print(f'O produto mais barato foi [{produto_barato}], custando R$[{menor_preco}]'.title())
print()