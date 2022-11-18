#Desenvolva um programa que leia o comprimento de três retas 
#e diga ao usuário se elas podem ou não formar um triângulo

med1 = float(input('Digite a primeira medida: '))
med2 = float(input('Digite a segunda medida: '))
med3 = float(input('Digite a terceira medida: '))

if med1 < med2 + med3 and med2 < med1 + med3 and med3 < med1 + med2:
    print('As medidas formam umm triangulo')
else:
    print('As medidas não formam um triangulo')