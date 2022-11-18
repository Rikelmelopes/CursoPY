#Crie um programa que leia um número inteiro e mostre na tela
#  se ele é PAR ou ÍMPAR.

numero = int(input("Digite o numero : "))

if (numero % 2) == 0:
    print("O numero {} é par!!".format(numero))
else:
    print("O numero {} é impar!!".format(numero))