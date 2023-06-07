#Nessa aula, vamos aprender como criar estruturas condicionais aninhadas, usando os comandos if.. elif.. else em programas Python.
#Aula 12 – Condições Aninhadas
nome = str(input("Qual o seu nome? \n")).upper().lower().strip()
if nome == "JAIRO":
    print("O seu nome é muito bonito.")
elif nome ==  "PEDRO" or nome == "MARIA" or nome == "PAULO":
    print("Seu nome é bem popular no Brasil")
elif nome in 'Ana Claudia Jéssica juliana':
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal.")
print(f"Tenha um bom dia, {nome}!")