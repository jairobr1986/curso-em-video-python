#DESAFIO DE PINTAR A PAREDE

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
print('Sua parede tem a dimensão de {} x {}, e a sua área é de {}m². '.format(largura, altura, area))
tinta = area/2
print('Para pintar essa parede, você precisará de {}L de litros de tintas. '.format(tinta))