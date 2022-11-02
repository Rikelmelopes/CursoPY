#escreva um programa que leia um valor em metros e o exiba
#convertido em centimetros e milimetros.

n1 = float(input("Digite o numero :"))
Centimetros = n1 * 100
Milimetros = n1 * 1000

print("Convertido em centimetros :{: .0f} cm\nConvertido em milimetros :{: .0f} mm".format(Centimetros,Milimetros))