#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome = input("Digite o nome :").strip()
print("Analisando seu nome ....")
print("Com letras minusculas fica : {}".format(nome.lower()))
print("Com letras maisusculas fica : {}".format(nome.upper()))
print("Seu nome tem {} letras".format(len(nome) - nome.count(' ')))
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))
