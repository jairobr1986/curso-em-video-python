# # Exercício 1 — Contagem simples
# # Faça um programa que mostre na tela os números de 1 até 10, um por linha, e no final escreva:
# print("Exercício 1");
# for repetidor in range(1, 11):
#     print(repetidor);
# print("Fim");
# # Exercício 2 — Contagem personalizada
# # Faça um programa que mostre na tela os números:
# print("-------------------");
# print("Exercício 2");
# for repetidor in range(0, 11, 2):
#     print(repetidor);
# print("Acabou");


# # Exercício 3 — Contagem regressiva
# # Faça um programa que mostre uma contagem regressiva de 10 até 0 e, no final, mostre:
# print("-------------------");
# print("Exercício 3");
# for repetidor in range(10, -1, -1):
#     print(repetidor);
# print("BOOM!")

# =============================================================================================

# Exercício 4 — Soma simples
# Faça um programa que mostre os números de 1 até 5 e, no final, mostre a soma deles.
# Saída esperada:
# 1
# 2
# 3
# 4
# 5
# Soma = 15
# 👉 Dica:
# Crie uma variável soma = 0
# Dentro do for, vá somando
# print("-------------------");
# print("Exercício 4");
# soma = 0;

# for c in range(1, 6):
#     print(c);
#     soma+= c;
# print(f"soma = {soma}");

# # =============================================================================================
# # 🟡 Exercício 5 — Tabuada (versão simples)
# # Faça um programa que mostre a tabuada do 3, de 1 até 10.
# # Saída esperada:
# # 3 x 1 = 3
# # 3 x 2 = 6
# # ...
# # 3 x 10 = 30
# # 👉 Dica:
# # Use for
# # Use multiplicação *
# print("-------------------")
# print("Exercício 5")
# for c in range(1, 11):
#     print(f'3 x {c} = {3*c}')

# # =============================================================================================
# # 🔵 Exercício 6 — Contagem com mensagem
# # Faça um programa que conte de 1 até 10, mas:
# # Mostre "Par" ao lado dos números pares
# # Mostre "Ímpar" ao lado dos números ímpares
# # Exemplo:
# # 1 Ímpar
# # 2 Par
# # 3 Ímpar
# # ...
# # 👉 Dica:
# # Aqui você vai precisar de if
# # Use o operador %
# print("-------------------")
# print("Exercício 6")

# for c in range(1, 11):
#     if c % 2==0 :
#         print(f"{c} é par.")
#     else:
#         print(f"{c} é impar")
# =============================================================================================

# Exercício 7 — Soma apenas dos pares
# Mostre os números de 1 até 10
# Some apenas os pares
# No final, mostre a soma
# 👉 Saída esperada:
# 2
# 4
# 6
# 8
# 10
# Soma dos pares = 30

print("-------------------")
print("Exercício 7")

somar_pares = 0
total_numeros_pares = 0
for c in range(1, 11):
    if c % 2 == 0:
        print('(' , c, ')', end="")
        total_numeros_pares += 1
        somar_pares = somar_pares + c
print(f" {total_numeros_pares} números foram somados, A soma = {somar_pares}")

# =============================================================================================

# 🟡 Exercício 8 — Contagem personalizada
# Mostre os números de 5 até 50, pulando de 5 em 5
# 👉 Saída:
# 5
# 10
# 15
# ...
# 50
print("-------------------")
print("Exercício 8")

for c in range(5, 51, 5):
    print(c)

# =============================================================================================

# 🔵 Exercício 9 — Tabuada com escolha
# Crie uma variável:
# numero = 7
# Mostre a tabuada desse número de 1 até 10
# 👉 Exemplo:
# 7 x 1 = 7
# 7 x 2 = 14
# ...

print("-------------------")
print("Exercício 9")

escolha = int(input("Qual tabudada quer aprender? "))

for c in range(1, 11):
    print(f"{escolha} x {c} = {escolha * c }")
# =============================================================================================


