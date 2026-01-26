# Exercício 75 – Análise de dados em uma Tupla
# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado
#  e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Se eu conseguir explicar o código estou aprendendo.

# quantidade = int(input('Quantos valores deseja ler: '))

# numero_tupla = tuple(int(input(f'Informe o {contador + 1}º NUMERO: '))for contador in range(0, quantidade)) 

# print(f'Você pediu para guardar [{quantidade}] VALORES.')
# print(numero_tupla)
# if numero_tupla.count(9) == 1:
#     print(f'O valor [9] aprece [{numero_tupla.count(9)}] VEZ')
# elif numero_tupla.count(9) > 1:
#     print(f'O valor [9] aprece [{numero_tupla.count(9)}] VEZES')
# else:
#     print(f'O valor [9], Não foi Informado.'.upper())

# if 3 in numero_tupla:
#     print(f'O valor [3], está na posição [{numero_tupla.index(3) + 1}] da tela.')
# else:
#     print('O valor [3], Não foi informado.'.upper())



# pares = []
# # Apesar de pares está aqui na parte de cima ele recebe as informações que estão na parte de baixo do código
# # aqui foi criado uma lista vazia para receber o valore calculados pelo for, onde o iterador(contador) 
# # entra na lista pega posição por posição verifica se é par aí com o append joga o valor na lista
# for contado_par in numero_tupla:
#     if contado_par % 2 == 0:
#         pares.append(contado_par)

# if len(pares) > 1:
#     print(f'Os valores pares são: {pares}')
# elif len(pares) == 1:
#     print(f'O valor par é: {pares}')
# else:
#     print('Não foi informado valor PAR.')
# # Se o valor for par os prints que tratam plural e singular são ativados
# # o len percorre a lista pares verificando se tem algo la dentro 
# # se tiver valores ele retorna e cai em cada condicional
# print('fim do programa.'.upper())



























# numero = tuple(int(input(f'digite o [{contador}º número]: ')) for contador in range(1, 5))
# print(numero) # aqui eu decorei que contador vai rodar quatro vezes fazendo o for nessa linha
# #No meu entendimento é como se o variavel numero estivesse dentro do for o que não faz muito sentindo pra mim, mas é assim que o 
# # o python aceita 

# # numero2 = tuple(int(input(f'Digite um número: '))for _ in range(1,5)) 
# # print(numero) #Aqui eu entendi que tem de colocar o _ pra funcionar, sem eu ter de colocar a variavel do contador dentro do print


# print(f'O valor 9 apareceu [{numero.count(9)}] VEZES.') #count, vai contar quantos valores tem dentro da tupla
# if 3 in numero:
#     print(f'o valor 3 apareceu na posição [{numero.index(3)}]') #index como o valor que eu colocar dentro dos parenteses vai retornar
#     #a posição do que eu coloquei no parentese, porém repetir o mesmo número e só aparece o primeiro valor encontrado
# else:
#     print(f'O valor 3 não foi digitado.')

# for contador in numero: #Aqui nesse for o contador vai ler a tupla exemplo entra na primeira posição do contador é par guarda na variavel contador, o que eu não entendi é como ele acumula mais valores pares ao invés de substitui a variavel contador, só sei que faz isso porque deu certo e no video do professor também deu certo
#     if contador % 2 == 0:
#         print(f'Os número pares são: [{contador}]')
# print(f'Fim do Programa!'.upper())


# Exercício Python 075: Análise de Dados em uma Tupla
# Objetivo: Praticar métodos de tuplas (.count, .index) e filtros de listas.

# # 1. ENTRADA DINÂMICA
# # O Jairo criou uma forma inteligente de definir o tamanho da tupla.
# try:
#     quantidade = int(input('Quantos valores deseja ler: '))
# except ValueError:
#     print("Erro: Digite um número inteiro para a quantidade.")
#     quantidade = 0

# # Compreensão de Tupla: Lê, converte para int e guarda tudo de uma vez.
# numero_tupla = tuple(int(input(f'Informe o {c + 1}º NÚMERO: ')) for c in range(quantidade))

# print(f'\nVocê pediu para guardar [{quantidade}] VALORES.')
# print(f'Sua Tupla: {numero_tupla}')
# print("-" * 40)

# # A) ANÁLISE DO VALOR 9 (.count)
# # O método .count(x) retorna quantas vezes x aparece na tupla.
# qtd_nove = numero_tupla.count(9)
# if qtd_nove > 0:
#     prefixo = 'vez' if qtd_nove == 1 else 'vezes'
#     print(f'O valor [9] aparece [{qtd_nove}] {prefixo.upper()}.')
# else:
#     print('O VALOR [9] NÃO FOI INFORMADO.')

# # B) POSIÇÃO DO VALOR 3 (.index)
# # Importante: o .index(x) dá erro se o valor não existir, 
# # por isso o 'if 3 in numero_tupla' que você usou é obrigatório!
# if 3 in numero_tupla:
#     # Somamos +1 porque para o Python a primeira posição é 0.
#     posicao = numero_tupla.index(3) + 1
#     print(f'O valor [3] está na {posicao}ª posição.')
# else:
#     print('O VALOR [3] NÃO FOI INFORMADO.')

# # C) NÚMEROS PARES (Filtro com Lista)
# pares = []
# for n in numero_tupla:
#     if n % 2 == 0:
#         pares.append(n)

# # Tratamento de Plural/Singular usando len()
# total_pares = len(pares)
# if total_pares > 0:
#     msg = (f"O valor par é {len.pares}") if total_pares == 1 else (f"Os valores pares são")
#     print(f'{msg}: {pares}')
# else:
#     print('NÃO FOI INFORMADO VALOR PAR.')

# print("-" * 40)
# print('FIM DO PROGRAMA.')


# Exercício Python 075: Análise de Dados em uma Tupla
# Objetivo: Praticar métodos de tuplas (.count, .index) e filtros de listas.

# 1. ENTRADA DINÂMICA
try:
    quantidade = int(input('Quantos valores deseja ler: '))
except ValueError:
    print("Erro: Digite um número inteiro para a quantidade.")
    quantidade = 0

# Compreensão de Tupla: Lê, converte para int e guarda tudo de uma vez.
numero_tupla = tuple(int(input(f'Informe o {c + 1}º NÚMERO: ')) for c in range(quantidade))

print(f'\nVocê pediu para guardar [{quantidade}] VALORES.')
print(f'Sua Tupla: {numero_tupla}')
print("-" * 40)

# A) ANÁLISE DO VALOR 9 (.count)
qtd_nove = numero_tupla.count(9)
if qtd_nove > 0:
    prefixo = 'vez' if qtd_nove == 1 else 'vezes'
    print(f'O valor [9] aparece [{qtd_nove}] {prefixo.upper()}.')
else:
    print('O VALOR [9] NÃO FOI INFORMADO.')

# B) POSIÇÃO DO VALOR 3 (.index)
if 3 in numero_tupla:
    posicao = numero_tupla.index(3) + 1
    print(f'O valor [3] está na {posicao}ª posição.')
else:
    print('O VALOR [3] NÃO FOI INFORMADO.')

# C) NÚMEROS PARES (Filtro com Lista)
pares = []
for n in numero_tupla:
    if n % 2 == 0:
        pares.append(n)

# Tratamento de Plural/Singular (Versão corrigida da sua sugestão)
total_pares = len(pares)
if total_pares > 0:
    # Ajustamos a mensagem dinamicamente
    msg = "O valor par encontrado foi" if total_pares == 1 else f"Os {total_pares} valores pares são"
    print(f'{msg}: {pares}')
else:
    print('NÃO FOI INFORMADO VALOR PAR.')

print("-" * 40)
print('FIM DO PROGRAMA.')