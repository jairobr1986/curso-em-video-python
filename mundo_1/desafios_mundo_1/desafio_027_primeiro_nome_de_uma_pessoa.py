#Exercício Python #027 - Primeiro e último nome de uma pessoa
#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.


#Esse funciona mas vou tentar exatamente como o professor fez
"""
nome = str(input("Digite o seu nome completo:\n")).upper() .strip()
nome1 = nome.split()
print(f"o seu nome completo é:\n{nome}")
print("O seu primeiro nome é {}.".format(nome1[0]))
print("E o seu ultimo nome é {}.".format(nome1[len(nome1)-1]))
"""

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print(f"Seu nome completo é: {n}")
print("Muito prazer em te conhecer!")
print("O seu primeiro nome é: {}.".format(nome[0]))
print("E o seu ultimo nome é: {}.".format(nome[len(nome)-1]))