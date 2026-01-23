#Exercício 38 – Comparando números
#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:– O primeiro valor é maior– O segundo valor é maior– Não existe valor maior, os dois são iguais

valor1 = int(input("Digite o primeiro valor:\n"))

valor2 = int(input("Digite o segundo valor:\n"))

if valor1 > valor2:
    print(f"O numero {valor1} é maior que o numero {valor2}.")
elif valor2 > valor1:
    print(f"O numero {valor2} é maior que {valor1}.")
else:
    print(f"\033[0;32;44m Os numeros são iguais\033[0m")
