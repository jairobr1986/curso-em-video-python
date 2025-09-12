# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:


# – Média abaixo de 5.0: REPROVADO

# – Média entre 5.0 e 6.9: RECUPERAÇÃO

# – Média 7.0 ou superior: APROVADO


print("Bom dia!!!")

nota1 = float(input("Digite a nota do 1º BIMESTRE:\n"))
nota2 = float(input("Digite a nota do 2º BIMESTRE:\n"))
media_notas = (nota1 + nota2) / 2

if media_notas < 5.0:
    print(f"A sua média foi {media_notas}, você foi REPROVADO.")
elif media_notas == 5.0 or media_notas > 5.0 and media_notas <= 6.9:
    print(f"A sua média é {media_notas}, e você está de RECUPERAÇÃO.")
elif media_notas >= 7.0:
    print(f"Parabéns!!!\n Sua média foi {media_notas}, e você está APROVADO.")
    