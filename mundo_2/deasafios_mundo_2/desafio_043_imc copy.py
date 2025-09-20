# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros


print(28*"-")
print(f"{' PAGAMENTOS ABAIXO!!! ':=^28}")

print(28*"-")
print("""
[1] DINHEIRO / CHEQUE -> 10% DESCONTO
[2] CARTÃO A VISTA -> 5% DESCONTO
[3] CARTÃO EM 2X -> VALOR NORMAL
[4] CARTÃO EM 3X OU MAIS -> 20% JUROS
""")
opcao_cliente = int(input("Escolha a forma de pagamento:\n".title()))
valor_compra = float(input("Valor Total:\n".upper()))

if opcao_cliente == 1:
    desconto = valor_compra - (valor_compra * 10 / 100)
    economia = valor_compra - desconto
    print(f"Pagando a vista com DINHEIRO ou CHEQUE você pagara {desconto:.2f} R$, e enconomizará {economia:.2f} R$.")
elif opcao_cliente == 2:
    desconto = valor_compra - (valor_compra * 5 / 100)
    economia = valor_compra - desconto
    print(f"Pagando a vista com DINHEIRO ou CHEQUE você pagara {desconto:.2f} R$, e enconomizará {economia:.2f} R$.")
elif opcao_cliente == 3:
    valor_normal = valor_compra / 2
    print(f"Parcelando em 2 vezes, você pagará {valor_normal:.2f} R$ daqui 30 dias e o valor de {valor_normal:.2f} R$ daqui 60 dias.")
elif opcao_cliente == 4:
    juros = valor_compra + (valor_compra * 20 / 100)
    juros_opcao = int(input("Quantas vezes quer parcelar: \n"))
    juros_parcelas = juros / juros_opcao
    economia =juros - valor_compra
    print(f"Parcelando em {juros_parcelas}, você pagará o valor total de {juros:.2f} R$, em {juros_opcao}X vezes do valor {juros_parcelas:.2f}, você deixou de ECONOMIZAR {economia:.2f} R$.")
else:
    desconto = valor_compra - (valor_compra * 10 / 100)
    economia = valor_compra - desconto
    print("Opção invalida, Tente Novamento com opção Válida")
    print(f"Sugestão, PAGAR a vista e ECONOMIZAR, {economia:.2f}")
