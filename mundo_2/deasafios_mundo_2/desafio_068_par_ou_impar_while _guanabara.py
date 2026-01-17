# Exercício 68 – Jogo do Par ou Ímpar
# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint #biblioteca nativa do python, inportando apenas gerador aleatorio de numeros inteiros

print(f"{' Exercício 68 – Jogo do Par ou Ímpar ':=^49}".upper())
print()
print('jogo iniciado...'.title())
print()


contador = 0

while True:

    computador = randint(0,10)
    derrota = 0
    while True:

        escolha = str(input('Jogador escolha [P] para [PAR] ou [I] para [IMPAR] \n')).strip().upper()[0]

        if escolha in 'PI':
            break
        else:
            print('='*49)
            print('atenção!'.upper())
            print('Informe apenas [P] -> [PAR] ou [I] -> [IMPAR] \nTENTE NOVAMENTE!\n')
            print('='*49)
        
    #Ajustando o visual  
    if escolha == 'P':
        escolha = '[PAR]'
    elif escolha == 'I':
        escolha = '[IMPAR]'

    while True:
        try:
            pessoa = int(input(f'Você escolheu {escolha}, \nAgora escolha o seu número:'.title()))

            if pessoa >= 0:
                break

            if pessoa < 0:
                print(f'Você informou {pessoa}, e números negativos não é permetido.'.upper())
                print('='*49)

            else:
                print('='*49)
                print('atenção!'.upper())
                print('entrada invalida!'.upper())
                print('='*49)

        except ValueError:
            print('='*49)
            print('atenção!'.upper())
            print('Apenas digite número inteiros \nTENTE NOVAMENTE!')
            print('='*49)
    
    soma = computador + pessoa

    if (escolha == '[PAR]') and (soma % 2 == 0):
        print(f'JOGADOR você venceu! Escolheu {pessoa} e eu {computador}, e a soma {soma} é [PAR].')
        contador += 1
    elif (escolha == '[IMPAR]') and (soma % 2 != 0):
        print(f'JOGADOR você venceu! Escolheu {pessoa} e eu {computador}, e a soma {soma} é [IMPAR].')
        contador += 1
    else:
        nova_conta = "par" if soma % 2==0 else "impar"
        print(f'COMPUTADOR venceu! JOGADOR  Escolheu {escolha} e o número {pessoa} e o COMPUTADOR {computador}, e a soma {soma} {nova_conta}.')
        derrota = 1
        break

print(f'JOGADOR você teve uma sequência de [{contador}] vitórias')
print(f"{'Programa finalizado!'}".upper())