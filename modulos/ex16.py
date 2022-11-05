#crie um programa que leia um numero real qualquer pelo 
#teclado e mostre na tela sua porção inteira


import math
n1 = float(input("Digite o numero = "))
print("A porção inteira do numero {} é igual a {}".format(n1,math.trunc(n1)))

