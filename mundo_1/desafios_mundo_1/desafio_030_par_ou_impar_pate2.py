# Exercício Python #030 - Par ou Ímpar? 
#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input("Digite um numero: \n"))
num1 = (num // 2) * 2
resultado = num - num1

if resultado == 1:
    print(f"o numero {num}, é impar.")
else:
    print(f"O numero {num}, é par.")

#     Dividir 7 por 2:

#    7 ÷ 2 = 3
#    3 × 2 = 6
#    7 - 6 = 1 (resto)
