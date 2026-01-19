#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('Primeiro nome a ser escolhido: '))
n2 = str(input('Segundo nome a ser escolhido: '))
n3 = str(input('terceiro nome a ser escolhido: '))
n4 = str(input(' Quarto nome a ser escolhido: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem para o trabalho será: ')
print(lista)