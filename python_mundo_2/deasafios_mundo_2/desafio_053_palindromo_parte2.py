# Exercício 53 – Detector de Palíndromo
# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

# APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

palindromo = str(input("Digite a frase: \n")).strip().upper()
print(f"Você digitou a frase {palindromo}")
print("------------------------")

separar_palavras = palindromo.split()
print(f"As frase com palvaras separadas é:\n{separar_palavras}")
print("------------------------")

juntar_palavras = "".join(separar_palavras)
print(juntar_palavras)
print("------------------------")

inverso = juntar_palavras[::-1]
# for letra in range(len(juntar_palavras) -1, -1, -1):
#     # print(juntar_palavras[letra])
#     inverso += juntar_palavras[letra]

print("\n",juntar_palavras, "\n", inverso)

print("------------------------")
if juntar_palavras == inverso:
    print("É um PALINDROMO")
else:
    print("Não é Palindromo.")