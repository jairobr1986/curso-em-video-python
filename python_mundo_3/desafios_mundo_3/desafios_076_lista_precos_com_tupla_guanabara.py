# Exercício 76 – Lista de Preços com Tupla
# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos
#  e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, 
# organizando os dados em forma tabular.

produtos_e_precos = ('Caderno', 2, 'Livro', 5, 'Lapis', 1, 'Caneta', 1.50, 'Borracha', 0.50)

print()
print('='*70)
print(f"{' Exercício 76 – Lista de Preços com Tupla ':=^70}")
print('='*70)

for contador in range(0, len(produtos_e_precos)):
    if contador % 2 == 0:
        print(f'{produtos_e_precos[contador]:.<21}',end='')
    else:
        print(f'R${produtos_e_precos[contador]:>7.2f}')
print()        
print('Fim do programa.'.upper())
