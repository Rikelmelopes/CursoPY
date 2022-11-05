#Faça um programa que leia o comprimento do cateto oposto
#e do cateto adijacente de um triangulo retangulo ,calcule
#e mostre o comprimento da hipotenusa.

#Primeira forma com importação

import math

co = float(input("Comprimento do cateto oposto : "))
ca = float(input("Comprimento do cateto adjacente : "))
hi = math.hypot(co,ca)

print("A hipotenusa dos catetos é {: .2f} ".format(hi))

#segunda forma de fazer sem importação

co = float(input("Comprimento do cateto oposto : "))
ca = float(input("Comprimento do cateto adjacente : "))
hi = (co ** 2 + ca ** 2) ** (1/2)

print("A hipotenusa dos catetos é {: .2f} ".format(hi))

#terceira forma 

from math import hypot

co = float(input("Comprimento do cateto oposto : "))
ca = float(input("Comprimento do cateto adjacente : "))
hi = hypot(co,ca)

print("A hipotenusa dos catetos é {: .2f} ".format(hi))
