lanche = ('Hamburguer', 'Suco','Pizza',  'Pudin', 'Batata Frita')
# lanche[1] = 'refrigerante' 
# print(lanche[:2])
print()
print('='*70)
contador = 0

for contador_da_lista in range(0, len(lanche)):
    print(f'ID: [{contador_da_lista}] item [{lanche[contador_da_lista]}]')

print('='*70)

for contador_da_lista in lanche:
    contador += 1
    print(f'ID: {contador} Referencias: {contador_da_lista}')

print('='*70)

for posicao, contador in enumerate(lanche):
    print(f'ID NUMERO: {posicao} Referencias: {contador}')


print('='*70)
print(sorted(lanche))
print('='*70)
print(lanche)
