# Exercício Python 48: Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

#separar números impares - feito
#somar multiplos de 3 
#intervalo de 1 até 500 - feito
contador = 0
contador2 = 0
somar = 0
somar2 = 0
for intervalo in range(1, 501, 2):
    somar2 += intervalo
    contador2 += 1

    if intervalo % 3 == 0:
        contador += 1
        somar += intervalo

print(f"A soma dos {contador} é valores solicitados são {somar}, e todos os numeros impares somados foram {somar2}, nesses valores {contador2}.do intervalo ")