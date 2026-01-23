# Exercício 55 – Maior e menor da sequência
# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.


# variveis para guardar o peso
maior_peso = 0
menor_peso = 0

for c in range(1, 6): #iniciando o contador em 5 rodadas
    
    peso_de_pessoa = float(input('Informe o seu peso: '))#variavel dentro do loop irá rodar 5 vezes porque está marcado de 1,6 no range

    if c == 1: #como o range começa em 1 contador vai ser 1 se fosse zero aqui teria de ser if c==0
        maior_peso = peso_de_pessoa # tanto essa variavel quanto a debaixo recebeu o primeiro valor informado
        menor_peso = peso_de_pessoa
    else: #a partir da segunda rodada começa a entradas nesse trecho do código
        if peso_de_pessoa > maior_peso:
            maior_peso = peso_de_pessoa
        if peso_de_pessoa < menor_peso:
            menor_peso = peso_de_pessoa

print(f'O maior peso foi {maior_peso}kg')
print(f'O menor peso foi {menor_peso}kg')

