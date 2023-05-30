#034 - Aumentos múltiplos
#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input("Digite o seu salário atual, para saber o seu aumento. \n"))
aumento10 = salario + (salario * 10 /100 )
aumento15 = salario + (salario * 15 / 100)
if salario <= 1250:
    print(f"O seu novo é {aumento15}, e você teve um aumento de 15%.")
else:
    print(f"O seu novo salario é {aumento10}, e você teve um aumento de 10%.")