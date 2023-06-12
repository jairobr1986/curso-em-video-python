# Exercício Python #037 - Conversor de Bases Numéricas 
#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input("Digite um numero para conversão: \n"))
print(""" Escolha uma das bases para conversão:

[1] converter para BINARIO
[2] converter para OCTAL
[3] coverter para HEXADECIMAL
""")
opcao = int(input("Sua opção: \n"))
if opcao == 1:
    print(f"O número {opcao} em BINARIO É {bin(num)[2:]}.")
    #esse trecho [2:] no código faz com que os dois primeiros caracteres não apareça no código quando quiser que algo não apareça só usar isso
elif opcao == 2:
    print(f" O numero {opcao} em OCTAL é {oct(num)}[2:].")
elif opcao == 3:
    print(f"O número {opcao} em HEXADECIMAL é {hex(num)}[2:].")
else:
    print("Opção inválida tente novamente com uma das opções acima!")