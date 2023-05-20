#Exercício Python #026 - Primeira e última ocorrência de uma string
#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase:")).upper() .strip()
print(f"A letra A aparece na frase {frase.count('A')} vezes.")
print("A primeira letra A aparece na posição {}.".format(frase.find('A') + 1))
print("A ultima letra A aparece na posição {}.".format(frase.rfind("A") + 1))

#Acima eu quis usar tanto format quanto o f pra ficar aprimorando.