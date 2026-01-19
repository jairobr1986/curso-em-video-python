#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual o valor do produto? R$ '))
novo = preco - (preco * 5 / 100)
print(' O produto que tem o valor {:.2f} R$, na promoção de 5% de desconto vai custar {:.2f} R$ '.format(preco, novo))