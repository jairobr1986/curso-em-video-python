#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# Exercício Python #039 - Alistamento Militar 

from datetime import date
ano_atual = date.today().year
print("\033[1;30;44m #####-ALISTAMENTO MILITAR-#####\033[0m")
ano_nascimento = int(input("\033[1;30;48mAno de nascimento:\033[0m\n")) 
idade_atual = ano_atual - ano_nascimento
print(f"Quem nasceu em {ano_nascimento}, tem {idade_atual} ano(s) em {ano_atual}")
if idade_atual < 18:
    alistamento = 18 - idade_atual
    ano_alistamento = ano_atual + alistamento
    print(f"Você tem {idade_atual} ano(s) ainda não pode se alistar.")
    print(f"Para seu alistamento ainda falta(m) {alistamento} ano(s) e será no ano de {ano_alistamento}")
elif idade_atual > 18:
    alistamento = idade_atual - 18
    ano_alistamento = ano_atual - 18
    print(f"você tem {idade_atual} ano(s) ja devia ter se alistado há {alistamento} ano(s) atrás.")
    print(f"O seu alistamento foi no {ano_alistamento}, portanto procure o mais rápido fazer o alistamento.")
else:
    print(f"Você tem {idade_atual} anos deve se alistar esse ano.")
