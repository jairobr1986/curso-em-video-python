n1 = int(input('Um valor: '))
n2 = int(input('Outro valor '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
exp = n1**n2

print('A soma é {}, a multipolicação é {} e a divisão é {:.3f}'.format(s, m, d))
#Aqui foi colocado entre as chaves{:.3f} que significa o seguinte
#.3f(ponto três flutuante ou seja quando a conta for feita se tiver
#mais de tres numeros depois do ponto será mostrado para o usuario apenas
# três)
print('Divisão inteira é {} e potência {}'.format(di, exp))
