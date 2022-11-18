tempo = int(input("Quantos anos tem seu carro ? "))

if tempo <=3:
    print("Seu carro é novo")

else: 
    print("Seu carro é velho")

#jeito simplificado

tempo = int(input("Quantos anos tem seu carro ? "))
print("carro novo" if tempo <=3 else "carro velho")
print("--FIM--")

nome = str(input("Digite seu nome :"))
if nome == "Rikelme":
    print("Seu nome é lindo")

else:
    print("nomezinho sem sal em !!")
print("Bom dia , {}".format(nome))

n1 = float(input("Digite a primera nota : "))
n2 = float(input("Digite a segunda nota : "))

nota = (n1 + n2) /2

print("levando em conta suas duas notas , a media final foi {}".format(nota))

if nota >= 6:
    print("Parabens voce passou !!")

else:
    print("Infelizmente voce ficou de recuperação")