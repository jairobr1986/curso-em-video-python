# Exercício 72 – Número por Extenso
# Exercício Python 72: Crie um programa que tenha uma dupla 
# totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

#criar uma tupla
numeros_extenso = (
    "zero", "um", "dois", "três", "quatro", "cinco", 
    "seis", "sete", "oito", "nove", "dez", "onze", 
    "doze", "treze", "quatorze", "quinze", "dezesseis", 
    "dezessete", "dezoito", "dezenove", "vinte"
)

# leitor = int(input('Digite um número: '))

# for contador in range(0, len(numeros_extenso)): #Aqui o range vai começar em zero ler toda a variavel numeros extenso
#     print(numeros_extenso[leitor]) #Aqui o numero extenso vai receber o valor do input e informar o nome que está na posição da tupla 
#     break
# #Acima eu fiz sem copiar
#Saber o tamanho da tupla
# print(len(numeros_extenso)) 

# #Abaixo eu fiz olhando o video e corrigindo
while True:
    try:
        leitor2 = int(input('Digite um número: '))

    except ValueError:
        print(f'[ERROR], APENAS NÚMEROS INTEIROS SÃO ACEITOS')
        continue

    if 0 <= leitor2 <= 20:
            break
    elif leitor2 > 20:
        print(f'Você informou um número [{leitor2}] MAIOR QUE 20')
    else:
        print(f'Você informou um número [{leitor2}] NEGATIVO')
 

print(f'Você digitou [{leitor2}] = [{numeros_extenso[leitor2]}]')


