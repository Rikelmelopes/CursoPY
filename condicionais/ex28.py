#Escreva um programa que faça o computador “pensar” em um 
# número inteiro entre 0 e 5 e peça para o usuário tentar 
# descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou 
# perdeu.

import random 

print(12 * "-----" )

print("Vou sortear um numero entre 0 e 5 .Tente adivinhar!!")

print(12 * "-----" )

n = int(input("Digite um numero entre 0 e 5 : "))
numero = random.randint(0,5) #randint sorteia numeros

print("o numero sorteado foi : {}".format(numero))

print(12 * "-----" )

if n == numero:
    print("Parabens voce acertou !!!")
else:
    print("Não foi dessa vez amigo :( , pensei no numero {} e não no {}".format(numero,n))