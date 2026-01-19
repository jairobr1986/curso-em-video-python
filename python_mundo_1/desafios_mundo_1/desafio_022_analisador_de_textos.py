"""Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome."""

nome = str(input("Digite seu nome completo:\n")).strip()
print("Analisando seu nome...")
print(f" seu nome em maiúsculo é {nome.upper()}.")
print(f" seu nome em minúsculo é {nome.lower()}.")
print(f" Seu nome ao todo tem {len(nome) - nome.count(' ')} letras.")
print(f" Seu primeiro tem {nome.find(' ')}")

#Abaixo outra forma de fazer quantas letras tem o nome
separa_nome = nome.split()
print(f" Seu primeiro nome é {separa_nome[0]} e ele tem {len(separa_nome[0])} letras")