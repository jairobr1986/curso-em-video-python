#035 - Analisando Triângulo v1.0
#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print("-=" * 20)
print(' Analisador de Triangulos')
print("-=" * 20)

r1 = float(input("Digite a primeira reta: \n"))
r2 = float(input("Digite a segunda reta: \n"))
r3 = float(input("Digite a terceira reta: \n"))
#A expressão dessa conta é para que o triangulo seja formado é umas das reta tem ser menor que as outras duas retas somadas
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("Analisando os valores informados, um triangulo pode ser formado. ")
else:
    print("Analisando os valores fornecidos não tem com se formar um triangulo.")