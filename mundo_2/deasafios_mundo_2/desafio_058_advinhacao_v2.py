# Exercício Python 58: Melhore o jogo do DESAFIO 28 
# onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.
# Exercício 58 – Jogo da Adivinhação v2.0

# from random import randint

# robo = randint(0, 10)
# nome = str(input('Qual o seu nome jogador: '))
# tentativas = 0
# jogador = None

# while jogador != robo:

#     jogador = int(input(f'Advinhe o número que eu pensei, entre [1 e 10]: '))

#     tentativas += 1
    
#     if jogador == robo:
#         print('Você venceu!')
#     if jogador > robo:
#         print(f'{nome}, DICA! Seu número é [MAIOR] do que o que eu pensei.')
#     if jogador < robo:
#         print(f'{nome}, DICA! Seu número é [menor] do que o que eu pensei.')



# print(f'PARABÉNS {nome}, Você acerto com {tentativas} tentativas')
# # Feito por mim sem assitir a resposta

# ===================================================================================
# Exercício Python 58: Melhore o jogo do DESAFIO 28 
# onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, 
# mostrando no final quantos palpites foram necessários para vencer.
# Exercício 58 – Jogo da Adivinhação v2.0

from random import randint

print('Vamos jogar um JOGO?'.upper())
print('Advinhe o número entre [0 e 10]: ')

robo = randint(0,10)
acertar = False
tentativas = 0

while not acertar:
    try:
        jogador = int(input('Informe o número que estou pensando: '.upper()))
        tentativas += 1
        if jogador == robo:
            acertar = True
        else:
            if jogador < robo:
                print(f'Mais... {jogador} é menor do que o número que pensei')
            else:
                print(f'Menos.. {jogador} é Maior do que o número que pensei')
    except ValueError:
        print('[ERROR] <-- Informe apenas números Inteiros')

print(f'{tentativas} tentativas, Parabéns!!! \n{jogador}, foi o número que pensei')


