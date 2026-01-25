# Exercício 75 – Análise de dados em uma Tupla

# Lendo os dados usando um loop (List Comprehension) e convertendo para tupla
# Isso facilita se amanhã você quiser ler 10 ou 100 números em vez de 4.
numeros = tuple(int(input(f"Digite o {i}º número: ")) for i in range(1, 5))

print(f"\nVocê digitou os valores: {numeros}")

# A) Quantas vezes apareceu o valor 9
print(f"O valor 9 apareceu {numeros.count(9)} vezes.")

# B) Posição do primeiro 3 (Com tratamento de erro)
if 3 in numeros:
    print(f"O valor 3 apareceu pela primeira vez na {numeros.index(3) + 1}ª posição.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")

# C) Quais foram os números pares
print("Os valores pares digitados foram: ", end='')
for n in numeros:
    if n % 2 == 0:
        print(f"{n} ", end='')

print("\n" + "="*40)