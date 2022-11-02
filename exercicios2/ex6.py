#crie um algoritimo que leia um numero e mostre o seu dobro
#triplo e raiz quadrada.

n1 = int(input("digite o numero :"))
dobro = n1 * 2
triplo = n1 * 3
raizQuadrada = n1 ** 0.5
raizQuadrada2 = n1 ** (1/2)

print("O dobro do numero escolhido é :{}\nO triplo do numero escolhido é:{}\nA raiz quadrada do numero escolhido é:{: .2f}\nA raiz quadrada do numero escolhido é:{: .2f}".format(dobro,triplo,raizQuadrada,raizQuadrada2))