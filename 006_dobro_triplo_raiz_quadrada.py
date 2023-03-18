#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e
#raiz quadrada
n = int(input('digite um numero: '))
d = n * 2
t = n * 3
r = n **(1/2)
print('o dobro de {}. vale {}. '.format(n, d))
print('O triplo de {} vale {}. \n e a raiz quadrada de {} é igual á {:.2f}. '.format(n, t, n, r))
