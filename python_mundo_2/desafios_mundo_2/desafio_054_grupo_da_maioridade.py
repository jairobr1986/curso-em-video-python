# Exercício 54 – Grupo da Maioridade

# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
contador_maior_idade = 0
contador_menor_idade = 0

print(ano_atual)
for c in range(1, 8):
    ano_nascimento = int(input('Em que ano você nasceu? '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        # print(f'Você tem {idade} anos, e é maior de idade')
        contador_maior_idade+= 1

    else:
        # print(f'Você tem {idade} anos, ainda é menor de idade')
        contador_menor_idade += 1


print(f'{contador_maior_idade} pessoas são maiores de 18 anos')
print(f'{contador_menor_idade} pessoas são menores de 18 anos')