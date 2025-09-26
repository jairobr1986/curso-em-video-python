# Exercício Python 50: Desenvolva um programa que leia seis números inteiros
#  e mostre a soma apenas daqueles que forem pares.
#  Se o valor digitado for ímpar, desconsidere-o.

lista = []
for numeros in range(1,7):
    num_i_p = int(input("Digite um número: "))
    
    if num_i_p % 2 == 0:
        lista.append(num_i_p)
print(lista)