# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep
print(f"{' GAME JOKENPO ':=^28}")
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0,2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
print("-="*11)
jogador = int(input("Qual é a sua jogada?\n"))
print(f"{' JO ':=^7}");sleep(0.5)
print(f"{' KEN ':=^7}");sleep(0.5)
print(f"{' PÔ!!! ':=^7}");sleep(0.5)
print("-="*11)
print(f"O computador jogou {itens[computador]}")
print(f"O jogador jogou {itens[jogador]}")
print("-="*11)

if computador == 0: #COMPUTADOR jogou PEDRA
    if jogador == 0:
        print("EMPATE!!!")
    elif jogador == 1:
        print("JOGADOR VENCE!!!")
    elif jogador == 2:
        print("COMPUTADOR VENCE!!!")
    else:
        print("jogada invalida!!!".upper())

elif computador == 1: #COMPUTADOR jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE!!!")
    elif jogador == 1:
        print("EMPATE!!!")
    elif jogador == 2:
        print("JOGADOR VENCE!!!")
    else:
        print("jogada invalida!!!".upper())
    
elif computador == 2: #COMPUTADOR jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE!!!")
    elif jogador == 1:
        print("COMPUTADOR VENCE!!!")
    elif jogador == 2:
        print("EMPATE!!!")
    else:
        print("jogada invalida!!!".upper())