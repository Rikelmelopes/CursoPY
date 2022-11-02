#Faça um algoritimo que leia o slario de um funcionario
#e mostre seu novo salario com 15% de aumento

salario = float(input("Qual é o seu salario ? R$"))
calculo = salario +(salario* 15/100)

print("Seu salario de R${: .2f} com o aumento de 15 porcento fica R${: .2f}".format(salario,calculo))