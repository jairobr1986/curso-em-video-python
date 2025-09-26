# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('Digite um numero para ver sua tabudada: '))
# print('-' *12)
# for contador_tabuada in range(1, 11):
#     print('{} x {:2} = {} '.format(num, contador_tabuada, num*contador_tabuada))
# print('-' *12)

print("---------------------")
for cont_tab in range(1, 11):
    print(F"{num} x {cont_tab} = {num*cont_tab}")
print("---------------------")