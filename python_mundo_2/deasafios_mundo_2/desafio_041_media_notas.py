# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

# abaixo meu código sem ajuda
from datetime import date

print("bom dia!!! ")

ano_nasc = int(input("Digite a data sua data de nascimento: \n"))

ano_atual = date.today().year

calculo = ano_atual - ano_nasc

if  calculo <= 9:
    print(f"Você tem {calculo} anos, e ficará na categoria MIRIM.")
if 9 < calculo <= 14:
    print(f"Você tem {calculo} anos, e ficará na categoria INFANTIL.")
if 14 < calculo <=19:
    print(f"Você tem {calculo} anos, e ficará na categoria JÚNIOR.")
if 19 < calculo <= 25:
    print(f"Você tem {calculo} anos, e ficará na categoria SÊNIOR.")
if calculo > 25:
    print(f"Você tem {calculo} anos, e ficará na categoria MASTER.")

