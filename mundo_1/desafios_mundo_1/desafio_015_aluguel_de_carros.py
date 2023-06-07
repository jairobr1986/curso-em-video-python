#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Quantos dias o carro permaneceu alugado? '))
km = float(input('Qual a quantidade de KM percorrido durante o período?'))
pagamento = (dias * 60) + (km * 0.15)
pagkm = km*0.15
pagdia = dias * 60
print('O total a ser pago é de R${:.2f}, sendo R${:.2f} em relação a quantidade de dias, e R${:.2f} em referente aos kms percorrido.'.format(pagamento,pagdia,pagkm))