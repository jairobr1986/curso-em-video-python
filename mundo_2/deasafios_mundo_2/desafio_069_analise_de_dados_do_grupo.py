# Exercício 69 – Análise de dados do grupo
# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 

# No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

pessoa_mais_18 = 0
homens = 0
mulhere_menos_20 = 0

print()
print(f"{' Exercício 69 – Análise de dados do grupo ':=^70}".upper())
print()

while True:

    try:
        idade = int(input('Qual a sua idade: ').title())
    except ValueError:
        print(f"{'[error] ! atenção !':=^70}".upper())
        print('Apenas informe números inteiros.')
        print('='*70)
        continue
    
    while True:
        sexo = str(input('Qual o seu sexo [M | F]: ')).strip().upper()[0]
        if sexo.isalpha() and sexo in 'MmFf':
            print(f"{' usuário cadastrado! ':=^70}".upper())
            print()
            break
        else:
            print(f"{'[error] ! atenção !':=^70}".upper())
            print('*** COMANDO INVALIDO! *** Apenas informe M ou F.')
            print('='*70)


    sexo = 'Masculino' if sexo in 'Mm' else 'Feminino'

    if idade > 18: 
        pessoa_mais_18 += 1
    
    if sexo == 'Masculino':
        homens += 1

    if (sexo == 'Feminino') and (idade < 20):
        mulhere_menos_20 += 1


    while True:
        print(f"{' Informe S para SIM ou N para NÃO: ':=^70}")
        sair = str(input('Deseja fazer um novo cadastro: ')).strip().upper()[0]
        if (sair.isalpha() and sair in 'Ss') or (sair.isalpha() and sair in 'Nn'):
            break
        else:
            print(f"{'[error] ! atenção !':=^70}".upper())
            print('*** COMANDO INVALIDO! *** Apenas informe S ou N.')
            print('='*70)

    if sair in 'Nn':
        break
print()
print(f"{'analise final':=^70}")
print()
print('A) quantas pessoas tem mais de 18 anos')
print(f'{pessoa_mais_18}, pessoa(as).')
print()
print('B) quantos homens foram cadastrados.')
print(f'{homens}, homem(ns)')
print()
print('C) quantas mulheres tem menos de 20 anos.')
print(f'{mulhere_menos_20}, mulher(es).')
print()
print(f"{' Programa finalizado! ':=^70}".upper())
