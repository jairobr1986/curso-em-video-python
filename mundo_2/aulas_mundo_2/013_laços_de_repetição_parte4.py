# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:


print(f"{' laços de repetição ':=^28}".upper())

somar_numero = 0

for var1 in range(0,4):
    num1 = int(input("Digite o número a ser somado:"))
    # somar_numero = somar_numero + num1
    somar_numero += num1
print(f"A soma de todos esses números é {somar_numero}.")