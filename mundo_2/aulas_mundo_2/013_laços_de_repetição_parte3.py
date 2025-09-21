# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:

print(f"{' laços de repetição ':=^28}".upper())

print('='*14)

lista = []

for var1 in range(0,3):
    num1 = int(input("Digite um valor:"))
    lista.append(num1)
    print((lista))
print(f"{' fim!!! ':=^21}".title())