# Exercício 67 – Tabuada v3.0
# Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, 
# para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

print(f"{' Exercício 67 – Tabuada v3.0 ':=^49}".upper()) # Mensagem de apresentação

# Abaixo loop infinito
while True:
    #Se eu tiver entendido certo o try mostrar a mensagem do except se for digitado qualquer coisa que seja diferente de um type int, 
    #No meu entendimento vai funcionar como se fosse um else, caso não seja int entre no except
    try:
        tabuada = int(input('Qual tabuada deseja aprender: '.title()))
        # Abaixo condição para sair do loop que está como infinito
        if tabuada < 0:
            break
        
        #abaixo contador for, não consegui fazer a tabuada com o while
        for contador in range(1,11):
            print(f'{tabuada:2} x {contador:02} = {tabuada*contador:02}')#:02 serve para colocar um zero antes do resultado e :2 serve para alinha para a direita deixando o primeiro espaço vazio
    except ValueError:
        print('Apenas digite valores inteiros')

print(f"{' Programa finalizado ':=^49}")
