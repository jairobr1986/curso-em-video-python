# Exercício 52 – Números primos
# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input("\033[0m Digite um número: "))
total = 0
for contador in range(1, num+1):
    if num % contador == 0:
        print(f"\033[33m",end="")
        total += 1
    else:
        print(f"\033[31m", end="")
    print(contador, end=" ")
print(total)
    