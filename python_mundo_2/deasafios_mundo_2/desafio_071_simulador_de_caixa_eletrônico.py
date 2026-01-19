# Exercício 71 – Simulador de Caixa Eletrônico

# Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print()
print('='*70)
print(f"{' Exercício 71 – Simulador de Caixa Eletrônico ': ^70}")
print('='*70)
print()
saque = int(input('Qual o valor a ser sacado: R$ '))
total_sacado = saque #Essa variavel ele está usando pra fazer calculo não sei porque ele não usou a  variaves saque
cedula_atual = 50 # o máximo que pede no enunciado
acumulador_cedula = 0 #gerar um contador de cédulas
print()

while True:
    # Lendo esse trecho na minha linguagem
    if  total_sacado >= cedula_atual: #Se o total sacado for maior ou igual a cedula de valor 50
        total_sacado -= cedula_atual # O total sacado vai fazer uma subtração do valor digitado meno 50
        #pensando que o total sacado seja 130, vai ficar 130-50, vai aconter uma volta no loop e depois vai ficar
        #80-50, vai dar outra volta no loop, e vai ficar um valor de 30
        acumulador_cedula += 1 # nessa linha, é um acumulador que vai contar de 0+1,+1,+1,+1,+1, infinitamente 
        #mas como a variavel que está sendo tratada dentro do if é 50 o acumulador está contando apenas as cedulas de 50
    else: # continuando o raciocinio pensando que tenho valor 30 ainda no total sacado, o meu primeiro if agora é falos pois 30 é meno que cedula atual
        #Como é false ele vai entrar no else, entrando no else a cedula tem valor 50, e como ela tem esse valor ela passa a se tornar 20, pois isso foi declarado
        #o programa volta para o primeiro if e pergunta: Se o total sacado for maior ou igual a cedula de valor 20
                                                        #O total sacado vai fazer uma subtração do valor 30 que está no total sacado  menos 20
                                                        #total sacado agora vale 10 e é maior que a cedula atual
                                                        #Agora o programa entra no else novamente, passa pelo 50, 
                                                        # passa pelo 20 e verifica que é igual a 20, 
                                                        # e cedula atual passa a valer 10
        
        if acumulador_cedula > 0: #Se o acumulador de cedula for maior que zero mostre ele na tela 
            print(f'Total de {acumulador_cedula} cédulas de R$[{cedula_atual}]')    

        #Esse trecho abaixo ficou confuso                                         
        if cedula_atual == 50:
            cedula_atual =20
        elif cedula_atual == 20: 
            cedula_atual = 10
        elif cedula_atual == 10:
            cedula_atual = 1
        acumulador_cedula = 0 # Essa parte eu não entendi porque o acumulador veio pra cá e não no inicio do else e porque zerou ele novamente
                                #no primeiro if o acumulador recebe ele + 1 e aqui está zerado

        if total_sacado == 0: #Nesse trecho total sacado que começa a ser comparado lá no primeiro if, agora que ele valer zero
                                # o while passa a ser false e para
            break