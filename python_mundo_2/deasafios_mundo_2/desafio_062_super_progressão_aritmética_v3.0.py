# Exercício 62 – Super Progressão Aritmética v3.0
# Exercício Python 62: Melhore o DESAFIO 61, 
# perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.


print(f"{' Progressão Aritmética v2.0 ':=^35}")
primeiro_numero = int(input('Digite o Primeiro número: '))
razao_pa= int(input('Informe a Progressão Aritmética '))

contador = 1
total = 0
mais_razao_pa = 10

while mais_razao_pa != 0:
    total += mais_razao_pa
    while contador <= total:
        print(f'-> {primeiro_numero} ', end="" )

        primeiro_numero+= razao_pa
        contador+=1
    print('\npausa'.upper())
    mais_razao_pa = int(input('Quantos termos quer mostar novamente: '))
print('\nFIM do programa'.upper())
print(f'Progessão finalizado com {total} termos exibidos.')    
