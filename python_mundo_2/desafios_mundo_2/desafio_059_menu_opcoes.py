# Exercício 59 – Criando um Menu de Opções
# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

print(f'{' valores ':=^21}')
valor1 = int(input('Informe um número: '))
valor2 = int(input('Informe outro número: '))

menu = 0

while menu != 5:

    menu = int(input('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
-------> :'''))

    if menu == 1:
        print(f' A soma de {valor1} + {valor2} = {valor1 + valor2}')
    elif menu == 2:
        print(f'{valor1} x {valor2} é igual {valor1 * valor2}')
    elif menu == 3:
        if valor1 > valor2:
            print(f'Entre {valor1} e {valor2}, o valor {valor1} é maior. ')
        elif valor1 == valor2:
            print(f'Os valores {valor1} e {valor2}, são iguais.') 
        else:
            print(f'Entre {valor1} e {valor2}, o valor {valor2} é maior. ') 
    elif menu == 4:
        valor1 = int(input('Informe um número: '))
        valor2 = int(input('Informe outro número: '))
    elif menu == 5:
        print('Saindo...')
    else:
        print('Opção Invalida!')

for c in range(5, 0, -1):
    print(c)
    sleep(0.5)
print('Obrigado, volte sempre.')


