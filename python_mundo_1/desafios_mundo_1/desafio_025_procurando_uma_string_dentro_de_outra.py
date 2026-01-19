#Exercício 25 – Procurando uma string dentro de outra
#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

#Desse jeito tem de usar aspas duplas e simples
"""
nome = str(input("Digite seu nome completo: \n"))
print(f" o nome {'SILVA' in nome.upper()}")

"""
#com o format do jeito normal não precisar ficar mudando aspas
nome = str(input("Diga seu nome completo: \n"))
print("o seu nome tem o sobrenome {}.".format("SILVA" in nome.upper()))