#Exercício Python #029 - Radar eletrônico
#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input("Digite a velocidade: \n"))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f"Você excedeu a velocidade e foi multado, \nportanto terá de pagar uma multa no valor de {multa:.2f} R$.\n")

print("Tenha uma ótima viagem e muito cuidado!")



"""
#Esse foi meu codigo feito antes de assistir a aula

velocidade = int(input("Qual a velocidade atual? \n"))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print(f"Voce foi multado e terá de pagar {multa} R$")

"""