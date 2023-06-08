#Exercício 36 – Aprovando Empréstimo
#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#Usuario vai inserir o valor da casa
valor_casa = float(input("Qual o valor da casa? \n R$: "))
#Usuario vai inserir o valor do salario
salario_comprador = float(input("Qual o seu salario? \n R$: "))
#Usuario vai inserir quantidade de anos que ele quer pagar
anos = int(input("Em quantos anos você quer pagar?\n"))
#calculo a ser feito abaixo:
#primeiro multiplica o anos que ele digitar por 12 meses colocando em parenteses
#Depois divide pelo valor da casa que será coloca na varivel de prestações
prestacoes = valor_casa / (anos * 12)
#minimo é a porcentagem de 30% do valor que é pedido pela empresa
minimo = salario_comprador * 30 / 100
#abaixo resultado na tela
print(f"Para pagar uma casa de R$ {valor_casa :.2f}, em {anos} anos ", end="") # Esse código entre parenteses (end="") serve para não fazer nada no final da linha, sendo assim vai juntar o meu print com o outro abaixo e vou poder usar a tela normal sem ter uma linha muito grande no codigo
print(f"a prestação será de R$ {prestacoes :.2f}")
if prestacoes <= minimo: #Se o calculo das prestações for menor ou igual ao minimo conceder emprestimo se não negar
    print("Emprestimo pode ser APROVADO!")
else:
    print("Emprestimo NEGADO!")