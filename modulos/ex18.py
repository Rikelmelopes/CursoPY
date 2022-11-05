#Faça um programa que leia um angulo qualquer e mostre na 
#na tela o valor seno,cosseno e tangente desse angulo.

from math import radians,sin,cos,tan

angulo = float(input("Digite o angulo que vc deseja : "))


seno = sin(radians(angulo))
print("o angulo de {} tem o seno de {: .2f}".format(angulo,seno))

cosseno = cos(radians(angulo))
print("o angulo de {} tem o cosseno de {: .2f}".format(angulo,cosseno))

tangente = tan(radians(angulo))
print("o anuglo de {} tem a tengende de {: .2f}".format(angulo,tangente))