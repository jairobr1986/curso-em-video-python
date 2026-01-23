# Exercício 68 – Jogo do Par ou Ímpar
# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint #biblioteca nativa do python, inportando apenas gerador aleatorio de numeros inteiros
import sys #biblioteca nativa do python, importando tudo do sistema, no windows o system32, e no linux não sei 

# computador = randint(0, sys.maxsize) #Gerando do zero até o último número que computador consegue gerar segundo a pesquisa que fiz na internet sys.maxsize, significa o último como estamos trabalhando com números inteiros imagino que gere até o ultimo, agora se maxsize se refirir somente a números aí tenho de saber ainda

print(f"{' Jogo do Par ou Ímpar ':=^49}".upper())
print()
print(f"{ ' Vamos jogar? ':=^49}")
print()
derrota = 0
resultado = None
par = 'Par'
impar = 'Impar'
soma_vitorias = 0
# computador = randint(0, sys.maxsize)
computador = randint(0, 10)

while True:

    while True: #tratando erro do jeito que eu sei, tentei usar .isalpha()
        escolha = str(input('Você escolhe [P] PAR ou [I] ÍMPAR? ')).strip().upper()[0]
        if not escolha in 'pPiI':
            print('Comando Invalido! \nescolha [P] PAR ou [I] ÍMPAR')
        if escolha in 'pPiI':
            break

    while True:        
        try:
            jogador = int(input('Eu escolho o número: '))
            if jogador >= 0:
                jogador = jogador
                break
            else:
                print('número negativos não são aceitos.'.upper())
        except ValueError:
            print('Apenas Números inteiros são aceitos. '.upper())


    if derrota == 1: 
        break

    resultado = computador + jogador    

    print('='*28)
    if escolha == 'P' and resultado % 2 == 0:
        print(f'Parabéns você escolheu {par} e venceu! \nVocê escolheu o numero {jogador} \nO computador escolheu {computador}')
        soma_vitorias += 1
        print()

    elif escolha == 'I' and resultado % 2 != 0:
        print(f'Parabéns você escolheu {impar} e venceu! \nVocê escolheu o numero {jogador} \nO computador escolheu {computador}')
        soma_vitorias += 1
        print()
    else:
        print(f'O computador venceu! \n Ele escolheu {computador} \nE você escolheu {jogador}')
        print()
        break

        
print()
if soma_vitorias == 0:
    print('Você perdeu de primeira.'.capitalize())
else:
    print(f'Você conseguiu {soma_vitorias} vitórias seguidas')

print(f"{'Programa Finalizado'}".upper())
