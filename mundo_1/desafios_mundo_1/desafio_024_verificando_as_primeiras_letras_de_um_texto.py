#Exercício 24 – Verificando as primeiras letras de um texto#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Digite a cidade que vocÊ nasceu:\n ")).strip()
#strip tira os espaços que existem na digitação
print(cidade[:5].upper() == "SANTO")
