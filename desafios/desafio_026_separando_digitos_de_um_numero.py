#Exercício 23 – Separando dígitos de um número
#Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input("Digite o numero desejado: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f"Analisando o numero {num}")
print(f"Unidade: {u}")
print(f"Dezenas: {d}")
print(f"Centenas: {c}")
print(f"Milhar: {m}")


#Abaixo jeito errado de fazer, mas da certo com quatro numeros embora terá erros com menos numero a não ser que seja feito ajustes.
"""
num = int(input("Digite o numero desejado: "))
n = str(num)
print(f"Analisando o numero {n}")
print(f"Unidade: {n[3]}")
print(f"Dezenas: {n[2]}")
print(f"Centenas: {n[1]}")
print(f"Milhar: {n[0]}")
"""