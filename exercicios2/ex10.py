#Crie um programa que leia quanto dinhero uma pessoa tem
#na carteira e mostre quantos dolares ela pode comprar
#considere (US1,00 = R$3,27)

dinheiro = float(input("digite o valor a ser convertido : RS$"))
dolar = dinheiro / 5.14
euro = dinheiro / 5.05

print("o valor {} convertido em dolar fica {: .2f}".format(dinheiro,dolar))
print("o valor {} convertido em euro fica {: .2f}".format(dinheiro,euro))