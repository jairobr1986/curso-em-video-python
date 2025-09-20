# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida
# - calculo do IMC: peso / (altura²) ou x/(x²)


print("Bom dia!!! \nVamos Calcular o seu IMC.")
print(28*"-")
peso = float(input("Digite o seu peso:\n"))
altura = float(input("Digite a sua altura:\n"))
imc = peso/(altura**2)
print(f"Seu peso é, {peso}, sua altura é {altura}, e seu IMC abaixo:")
if imc < 18.5:
    print(f"O seu IMC é {imc:.1f}, você está Abaixo do Peso")
elif imc >= 18.5 and imc < 25:
    print(f"O seu IMC é {imc:.1f}, você está com o Peso Ideal")
elif imc >= 25 and imc < 30:
    print(f"O seu IMC é {imc:.1f}, você está Sobrepeso")
elif imc >=30 and imc < 40:
    print(f"O seu IMC é {imc:.1f}, você está com Obesidade, cuidado inicie uma dieta.")
elif imc >= 40:
    print(f"O seu IMC é {imc:.1f}, você está com Obesidade Mórbida, e já deve procurar um profissional da saúde.")
