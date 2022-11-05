#um professor quer sortear um dos seus alunos para apagar
#o quadro. Faça um programa que ajude ele , lendo o nome
#deles e escrevendo o nome escolhido.

import random

al1 = input("Primeiro nome :")
al2 = input("Segundo nome :")
al3 = input("Terceiro nome :")
al4 = input("Quarto nome :")

lista = [al1,al2,al3,al4]
escolhido = random.choice(lista)

print("O aluno escolhido foi {} ".format(escolhido))

