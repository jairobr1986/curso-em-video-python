 #Crie um programa onde mostre o antecessor e sucessor do numero digitado
n = int(input('Digite um número: '))
an = n-1
su = n+1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {} .'.format(n, an, su))


''' Outra forma de fazer esse código é dessa forma, onde consome menos memória
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {} .'.format(n,(n-1),(n+1)))
'''
