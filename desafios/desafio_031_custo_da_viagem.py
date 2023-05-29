#Exercício 31 – Custo da Viagem
#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input("Quantos KM você prentende viajar? \n"))
if distancia <= 200:
    preco = distancia * 0.50
    print(f"A sua viagem custará R$ {preco:.2f}")
else:
    preco = distancia * 0.45
    print(f"A sua viagem terá o valor de R$ {preco:.2f}")