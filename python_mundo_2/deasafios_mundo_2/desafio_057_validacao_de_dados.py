# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
# mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
# Exercício 57 – Validação de Dados

sexo = None

while sexo not in ('F','M'):
    sexo = str(input('Informe o seu sexo M/F: ')).strip() .upper()
    if sexo not in ('F','M'):
        print('Opção invalida!')
    
if sexo == ('F'):
    print(f'O sexo:({sexo}) FEMININO, foi escolhido.')
if sexo == ('M'):
    print(f'O sexo:({sexo}), MASCULINO foi escolhido.')
