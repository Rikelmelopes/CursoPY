#Faça um programa que leia um número de 0 a 9999 e 
# mostre na tela cada um dos dígitos separados.

numero = int(input("Digite o numero :"))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
n = numero // 1000 % 10

print("Analisando o numero.... ".format(numero))
print("Unidade : {} ".format(u))
print("Dezena : {} ".format(d))
print("Centena : {} ".format(c))
print("Milhar : {} ".format(n))