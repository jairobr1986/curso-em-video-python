# Exercício 73 – Tuplas com Times de Futebol
# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. 
# Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.


times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
         'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
         'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
         'São Paulo', 'Fluminense', 'Sport Recife',
         'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
         'Atlético-GO')



print()
print(f"{'Exercício 73 – Tuplas com Times de Futebol':=^70}")
print()
print('a) Os 5 primeiros times.')
print()
print(times[0:5])
print('='*70)
print('b) Os últimos 4 colocados.')
print()
print(times[-4:])
print('='*70)
print('c) Times em ordem alfabética.')
print()
print(sorted(times))
print('='*70)
print('d) Em que posição está o time da Chapecoense.')
print()
print(f" O Chapecoense está na [{times.index('Chapecoense')+1}ª] POSIÇÃO")
print('='*70)
