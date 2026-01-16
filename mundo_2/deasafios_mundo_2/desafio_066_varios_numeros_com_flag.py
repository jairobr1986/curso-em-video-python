# Exercício 66 – Vários números com flag
# Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e 
# qual foi a soma entre elas (desconsiderando o flag).

# Variaveis com o mesmo valor colocamos sobre a outro com o mesmo valor

print(f"{' Exercício 66 – Vários números com flag ':=^49}")
soma = contador = 0 

while True:

    # incio do programa
    leia = int(input('Informe um número: '))
    # fim do programa
    if leia == 999:
        break

# Apartir de agora começa a logica
    contador += 1
    soma += leia
     
print(f'{contador} números foram inseridos. \nE a soma dos números é [{soma}]')
