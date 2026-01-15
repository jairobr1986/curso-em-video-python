# Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e
# qual foi a soma entre eles (desconsiderando o flag).

# minha versão abaixo

contador = soma = 0


while True:

    n = int(input('informe o número a ser lido: '))
    print('digite caso queira finalizar -> [999]'.capitalize())

    if n == 999: # pelo que entendi já posso iniciar o loop e colocar um break logo em seguida com uma condicional
        break #também não sei se é melhor colocar um break, aqui eu não sei se encerrar o loop ou apenas pausa, se vai consumir memoria ou energia
    
    if n != 999:
        soma += n #como soma está dentro da condição se digitar 999 ele não será somado, pelo que eu entendi
        contador += 1 # como o contado está dentro da condição if ele contarar as repetições de fora do if apenas dentro dele

print(f'Foram inseridos {contador} números, e a soma deles é {soma}') #Aqui é um print com f'string que dá pra usar variaves dentro das {}



##Versão chatGPT
# contador = 0
# soma = 0

# while True:
#     n = int(input('Informe um número (999 para parar): '))

#     if n == 999:
#         break

#     soma += n
#     contador += 1

# print(f'Foram inseridos {contador} números, e a soma deles é {soma}')
