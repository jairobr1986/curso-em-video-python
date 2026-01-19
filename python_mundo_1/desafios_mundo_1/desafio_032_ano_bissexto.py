#Exercício 32 – Ano Bissexto
#Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input("Digite o ano que você quer saber se é ou não BISSEXTO, ou digite 0 para analisar o ano atual: \n"))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é BISSEXTO.")
else:
    print(f"O ano de {ano}, não é BISSEXTO")