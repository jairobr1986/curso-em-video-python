# Exercício Python 51: Desenvolva um programa que leia o primeiro termo
#  e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

termo1 = int(input("Digite o termos da progressão: "))
razao = int(input("Digite a razão da Progressão Aritimetica: "))
decimo = termo1 + (10 - 1) * razao # 1º numero digitado + (10 - 1) * razao

print(f"A progressão atritimetica de {razao} em {razao} é:")

for var1 in range(termo1,decimo+1,razao):
    print(f"{var1}", end="-> ")
print("Acabou!!!")

