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

programa = None
nome_produto = None
preco_produto = 0
total_gasto = 0
produto_mais_1000 = 0

while True:
    
    while True:
        nome_produto = str(input('Nome do produto: '.upper())).strip().upper()
        
        #na minha leitura esse trecho se ler assim não sei é o correto:
        #se nome_produto for diferente de vazio e nome_produto em seu primeiro caractere for igual a uma letra entre a e z, pare o while
        if nome_produto != '' and nome_produto[0].isalpha():
            print()
            break
        else:
            print(f"{'[error] ! atenção !':=^70}".upper())
            print('*** PRODUTO INVALIDO! *** Esse campo aceita apenas palavras.')
            print('='*70)
    while True:
        try:
            print(f'Produto na sacola: {nome_produto}'.upper())
            preco_produto = float(input('Preço do produto: R$'.upper()))
            print('='*70)
            if preco_produto > 1000:
                produto_mais_1000 += 1
            break

        except ValueError:
            print()
            print(f"{' Atenção informe apenas valores EX: 1500.50':=^70}")
            continue

    while True:

        print(f'Produto na sacola: {nome_produto}'.upper())
        print(f'Preço do produto {preco_produto}R$')
        print()
        novo_produto = str(input('Deseja continuar \nS = [SIM] N = [NÃO]: '.upper())) .strip().upper()[0]
        if novo_produto in 'Ss':
            break
        if novo_produto in 'Nn':
            programa = 'sair'
            break
        else:
            print(f"{'[error] ! atenção !':=^70}".upper())
            print('*** PRODUTO INVALIDO! *** Esse campo aceita apenas S ou N.')
            print('='*70)

    total_gasto += preco_produto
    

    if programa == 'sair':
        break
    
print()
print(f"{' Programa Finalizado ':=^70}".upper())
print()
print('A) qual é o total gasto na compra.'.upper())
print(f'Total gasto em compras [{total_gasto}]R$.'.upper())
print()
print('B) quantos produtos custam mais de R$1000.'.upper())
print(f'{produto_mais_1000} produto(s) mais de 1000 R$')
print()

