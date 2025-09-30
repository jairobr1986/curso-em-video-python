# Exercício 52 – Números primos
# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("\033[0m Digite um número: "))
total_de_numeros_dividos = 0 #Aqui pra fazer a contagem no loop
for contador in range(1, num+1):
    if num % contador == 0:
        print(f"\033[33m",end="")
        total_de_numeros_dividos += 1
    else:
        print(f"\033[31m", end="")

    print(contador, end=(" "))
print("\n------")
print(f"o número {num}, foi divido {total_de_numeros_dividos} vezes.")
if total_de_numeros_dividos == 2:
    print(f"o {num} é um número PRIMO, pois ele foi dividido por 1 e por {num} ele mesmo.")
else:
    print(f"o número {num}, não é um número PRIMO.")