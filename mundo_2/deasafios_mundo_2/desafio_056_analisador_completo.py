# Exercício 56 – Analisador completo
# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e 
# quantas mulheres têm menos de 20 anos.

idades_somadas = 0
homem_mais_velho = 0
contador_mulher_menor_20 = 0
nome_mais_velho = ''

for c in range(1, 5):
    nome = str(input('Informe o seu nome:')).strip() .upper()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe o sexo com M ou F: ')).strip() .upper()

    idades_somadas += idade
    
    if homem_mais_velho == "":
        homem_mais_velho = "Não tem homem no grupo."
    if (idade > homem_mais_velho) and (sexo == 'M'):
        homem_mais_velho = idade
        nome_mais_velho = nome
    if (idade < 20) and (sexo == 'F'):
        contador_mulher_menor_20 += 1

media_de_idade = (idades_somadas) / 4        

print(f'O homem mais velho tem {homem_mais_velho} anos, e seu nome é {nome_mais_velho}.')
print(f'Nesse grupo tem {contador_mulher_menor_20} mulher(es), menor(es) de 20 anos')
print(f'A média de idade do grupo é {media_de_idade:.1f} anos')