# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, len(itens)-1)

print(f"{' JOKENPÔ ':=^28}")

jogador = int(input("""
Escolha:
[0] PEDRA
[1] PAPEL
[2] TESOURA
"""))
print(f"JOGADOR escolheu {jogador} e COMPUTADOR escolheu {computador}.")
print(f"{'':-^28}")
if computador == 0 and jogador == 0:
    print("COMPUTADOR PEDRA vs PEDRA JOGADOR. \nEMPATE!!!")
elif computador == 0 and jogador == 1:
    print("COMPUTADOR PEDRA vs PAPEL JOGADOR. \nJOGADOR VENCEU!!!")
elif computador == 0 and jogador == 2:
    print("COMPUTADOR PEDRA vs TESOURA JOGADOR. \nCOMPUTADOR VENCEU!!!")

elif computador == 1 and jogador == 1:
    print("COMPUTADOR PAPEL vs PAPEL JOGADOR. \nEMPATE!!!")
if computador == 1 and jogador == 0:
    print("COMPUTADOR PAPEL vs PEDRA JOGADOR. \nCOMPUTADOR VENCEU!!!")
elif computador == 1 and jogador == 2:
    print("COMPUTADOR PAPEL vs TESOURA JOGADOR. \nJOGADOR VENCEU!!!")
    
elif computador == 2 and jogador == 2:
    print("COMPUTADOR TESOURA vs TESOURA JOGADOR. \nEMPATE!!!")
elif computador == 2 and jogador == 1:
    print("COMPUTADOR TESOURA vs PAPEL JOGADOR. \nCOMPUTADOR VENCEU!!!")
elif computador == 2 and jogador == 0:
    print("COMPUTADOR TESOURA vs PEDRA JOGADOR. \nJOGADOR VENCEU!!!")
else:
    print("Digite um número valido.")