# Exercício 65 – Maior e Menor valores
# Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e 
# qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

perguntar = 'S'
maior = None
menor = None
contador = 0
media = 0
soma = 0

while perguntar in 'Ss':
    
    ler_numero = int(input('Informe os números: '.capitalize()))
    perguntar = str(input('Deseja continuar? \n[S] para SIM ou [N] para NÃO. '.upper())).strip()[0]
    contador += 1
    soma += ler_numero

# Se maior estiver vazio ou ler numero for maior do que maior coloque o maior valor na variavel maior
    if maior is None or ler_numero > maior:
        maior = ler_numero
# Se maior estiver vazio ou l
# er numero for menor do que menor coloque o menor valor na variavel maior
    if menor is None or ler_numero < menor:
        menor = ler_numero

#Aqui tipo que decorei não entendi muito bem, pra fazer a media
# media recebe a soma divido pelo contador, somente se o contado for maior do que zero, o else valendo zero que não entendi certo
media = soma / contador if contador > 0 else 0

print(f'O número [MAIOR] é [{maior}] \nO número [menor] é [{menor}]')
print(f'A media é {media}')



# perguntar = 'S'
# maior = menor = None
# contador = soma = 0

# while perguntar == 'S':
#     try:
#         ler_numero = int(input('Informe um número: '))
#         soma += ler_numero
#         contador += 1

#         if maior is None or ler_numero > maior:
#             maior = ler_numero
#         if menor is None or ler_numero < menor:
#             menor = ler_numero
            
#     except ValueError:
#         print("Erro: Digite apenas números inteiros.")
#         continue # Volta para o topo do loop principal

#     # --- LOOP DE VALIDAÇÃO (O loop interno) ---
#     while True:
#         resposta = input('Deseja continuar? [S/N]: ').strip().upper()
#         if resposta in ('S', 'N'):
#             perguntar = resposta # Atualiza a variável de controle principal
#             break # Sai apenas deste loop interno
#         print('Resposta inválida! Digite apenas S ou N.')
#     # ------------------------------------------

# media = soma / contador if contador > 0 else 0
# print(f'\nMAIOR: {maior} | MENOR: {menor} | MÉDIA: {media:.2f}')
