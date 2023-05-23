#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um numero de 0 á 5, Tente advinhar:")
print("-=-" * 20)

jogador = int(input("Em que numero eu pensei? \n"))
print("pensando...")
sleep(3)
if computador == jogador:
    print(f"PARABENS!!! Você pensou no numero {jogador} e eu também pensei no numero {computador} portanto... me venceu.")
else:
    print(f"Você perdeu eu pensei no numero {computador} e não no numero {jogador}.")













"""
#jeito errado de fazer

num = int(input("Digite um numero entre 0 e 5:\n "))
if num == 4:
    print(f"Você digitou {num}, portanto você venceu!")
else:
    print(f"Você digitou {num}, e perdeu mas pode tentar novamente.")


"""