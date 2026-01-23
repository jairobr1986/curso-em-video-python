# Exercício 61 – Progressão Aritmética v2.0
# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print(f"{' Progressão Aritmética v2.0 ':=^35}")
primeiro_numero = int(input('Digite o Primeiro número: '))
razao_pa= int(input('Informe a Progressão Aritmética '))

contador = 1

while contador <= 10:
    print(f'-> {primeiro_numero} ', end="" )

    primeiro_numero+= razao_pa
    contador+=1
print('\nfim'.upper())
