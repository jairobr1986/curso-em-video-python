# Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print(f"{' exibir numeros pares!!! ':=^35}")

num_inicio = int(input("Digite o inicio do intervalo:\n".capitalize()))
num_fim = int(input("Digite o final do intervalo:\n".capitalize()))
passo = int(input("digite o passo que você deseja:\n"))
print("="*28)

for var1 in range(num_inicio, num_fim, passo):
    if var1 % 2 == 0:
        print(var1)
    elif  var1 % 2 != 0:
        var1+= 1
        print(var1)
    