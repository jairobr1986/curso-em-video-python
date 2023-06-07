#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual o salário atual do funcionário? R$ '))
novosal = salario + (salario * 15 / 100)
print('Para o funcionário que está ganhando R$ {:.2f}m com 15% de aumento salarial, ele passará a receber R$ {:.2f} '.format(salario, novosal))
