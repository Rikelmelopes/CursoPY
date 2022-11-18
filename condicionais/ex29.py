#Escreva um programa que leia a velocidade de um carro. 
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo 
#que ele foi multado. A multa vai custar R$7,00 por cada Km 
#acima do limite

velocidade = float(input("Digite a velocidade : "))

print(12*"¨¨¨¨¨")

if velocidade <= 80:
    print("Voce esta dentro do limite,O limite da rodovia é 80KM/h")
else:
    multa = (velocidade - 80) * 7
    print("""Ao atravessar o radar a {}km/h\nvoce foi multado , o valor da sua multa é R${: .2f} """.format(velocidade,multa))