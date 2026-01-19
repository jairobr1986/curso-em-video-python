#Exercício Python #033 - Maior e menor valores 
#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input("Digite o Primeiro valor: \n"))
b = int(input("Digite o Segundo valor:\n"))
c = int(input("Digite o  terceiro valor: \n"))

if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f"O menor valor é {menor}, e o maior valor é {maior}")