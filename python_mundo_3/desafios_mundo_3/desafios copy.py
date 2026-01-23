# Exercício 72 – Número por Extenso
# Exercício Python 72: Crie um programa que tenha uma dupla 
# totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Exercício Python 72: Crie um programa que tenha uma dupla 

numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", 
    "seis", "sete", "oito", "nove", "dez", "onze", 
    "doze", "treze", "quatorze", "quinze", "dezesseis", 
    "dezessete", "dezoito", "dezenove", "vinte"
)

leitor = None

while True:

    try:

        leitor = int(input('Informe um número de 0 até 20: '))
        
    except ValueError:
        print(f'Você digitou [{leitor}], esse campo aceita apenas número inteiros.')
        continue

    if 0 <= leitor <= 20:
        for contador_extenso in range(0, len(numeros_extenso)):
        print(f'você digitou [{leitor}] = [{numeros_extenso[contador_extenso]}]')
        leitor = leitor
        break

    
    elif leitor > 20:
        print('Você informou um número Maior que 20. Tente Novamente!')
        continue
    else:
        print(f'Você informou um número negativo. Tente Novamente!')   
        continue
    

    if 0 <= leitor <= 20:
        break