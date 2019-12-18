nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
peso1 = float(input())
peso2 = float(input())

tpeso1 = peso1 / 100
tpeso2 = peso2 / 100
tpeso3 = (100-peso1-peso2) / 100
media = (nota1*tpeso1)+(nota2*tpeso2)+(nota3*tpeso3)

print("Média Final: {:.1f}".format(media))
