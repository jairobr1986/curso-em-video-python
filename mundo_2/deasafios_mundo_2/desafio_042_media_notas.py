# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print("-=" * 20)
print(' Analisador de Triangulos')
print("-=" * 20)

r1 = int(input("Digite a primeira reta: \n"))
r2 = int(input("Digite a segunda reta: \n"))
r3 = int(input("Digite a terceira reta: \n"))
#A expressão dessa conta é para que o triangulo seja formado é umas das reta tem ser menor que as outras duas retas somadas
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("Analisando os valores informados, um triangulo pode ser formado. ", end="")
    if r1 == r2 and r2 == r3:
        print(f"{r1}-> {r2}-> {r3}: formam um triangulo EQUILATERO.")
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print(f"{r1}-> {r2}-> {r3}: formam um triangulo ESCALENO.")
    else:
        print(f"{r1}-> {r2}-> {r3}: formam um triangulo ISÓSCELES.")


else:
    print("Analisando os valores fornecidos não tem com se formar um triangulo.")