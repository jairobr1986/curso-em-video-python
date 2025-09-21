# Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
print(f"{' contagem regressiva!!! ':=^28}")

mensagem = input("Qual mensagem você deseja no final da contagem?\n".title())
mensagem_final = " ".join(mensagem.split())
contagem = int(input("Digite quantos segundos deseja para a contagem regressiva:\n"))
print("iniciando contagem...".title())
for var1 in range(contagem, -1, -1):
    print(var1);sleep(1)
print(f"boom!!!!!\U0001f386 \U0001f387 \U0001f389 \U0001f38a \n{mensagem_final}".upper())