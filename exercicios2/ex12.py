#Faça um algoritimo que leia o preço de um produto
#e mostre seu novo preço ,com 5% de desconto

preco = float(input("qual é o preço ? R$"))
calculo = preco -(preco *5/100)

print("o valor R${} com o 5 porcento de desconto fica R${} ".format(preco,calculo))