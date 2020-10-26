# 119210934 - Karen A. A. Alves
# Cálculo do IMC


peso = float(input())
altura = float(input())

imc = peso / (altura**2)

if imc < 18.5: 
    print("IMC = {:.1f}\nClassificação = Magreza".format(imc))

elif 18.5 <= imc < 25: 
    print("IMC = {:.1f}\nClassificação = Saudável".format(imc))

elif 25 <= imc < 30: 
    print("IMC = {:.1f}\nClassificação = Sobrepeso".format(imc))

elif 30 <= imc: 
     print("IMC = {:.1f}\nClassificação = Obesidade".format(imc))

