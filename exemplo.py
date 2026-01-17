frase = str(input('Digite uma frase: ')).strip() .upper()
palavras_fatiada = frase.split()
juntar_palavras = "" .join(palavras_fatiada)
print(f'Você digitou: {palavras_fatiada}')
print(f'Você digitou: {juntar_palavras}')


