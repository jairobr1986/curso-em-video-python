# Nessa aula, vamos começar nossos estudos com os laços e vamos fazer primeiro o “for”, que é uma estrutura versátil e simples de entender. Por exemplo:

print(f"{' laços de repetição ':=^28}".upper())

inicio = int(input("incio:".title()))
fim = int(input("fim:".upper()))
passo = int(input("passo:".title()))

print('='*14)
for loop in range(inicio, fim+1, passo):
    print(loop)
print(f"{' fim!!! ':=^21}".title())