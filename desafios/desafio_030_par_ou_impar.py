# Exercício Python #030 - Par ou Ímpar? 
#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input("Digite um numero: \n"))
resultado = numero % 2
if resultado == 1:
    print(f"o numero {numero}, é impar.")
else:
    print(f"O numero {numero}, é par.")