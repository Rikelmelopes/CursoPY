#Faça um programa que leia a largura e a altura de uma parede
#em metros ,calcule a sua area e a quantidade de tinta necessaria
#para pinta-la, sabendo que cada litro de tinta pinta uma area
#de 2m²

largura = float(input("Digite a largura :"))
altura =  float(input("Digite a altura :"))
area = largura * altura
tinta = area / 2
print("Sua parede tema dimesão de {}x{} e sua area é de {} ,vai ser preciso de {}L de tinta para pintar a parede.".format(largura,altura,area,tinta))