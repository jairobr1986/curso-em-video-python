# Exercício 77 – Contando vogais em Tupla
# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python',
'curso', 'grátis', 'estudar', 'praticar',
'trabalhar', 'mercado', 'programador', 'futuro')

for contador in palavras:
    print(f'\nEm {contador.upper()} temos as vogais: ',end=' ')
    for letras in contador:
        if letras.lower() in 'aeiou':
            print(letras,end=' ')

# Dissecando o código
# tupla palavras
# for criando um contador que percorre a tupla palavras
# mostra na tela cada palavra que está sendo lida começando pela posição zero
# e mostrando cada palavra, depois o end quebra uma linha no qual fica meio confuso porque 
# é como se fizesse um concatenação com o for de baixo, mas como esse video eu apenas copiei não entendi
# a explicação do professor
# no outro for como todo for tem de ter um contador, tem um contador no qual ele informou que agora percorre as palavras e o if 
# o if eu já conheço, o if está verifica se o contador é true na vogais aeiou, se for true
# cai no print, apenas as vogais, mas não entendi        