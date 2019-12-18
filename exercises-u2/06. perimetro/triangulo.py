#UFCG
#PROG1
#KAREN A. A. ALVES

import math 

x1 = int(input())    # coordenadas  # A
y1 = int(input())                   
x2 = int(input())    # triangulo    # B
y2 = int(input())
x3 = int(input())                   # C
y3 = int(input())

dAB = math.sqrt((((x1 - x2)**2) + ((y1 - y2)**2)))  # Distancia AB (coordenadas)
dBC = math.sqrt((((x2 - x3)**2) + ((y2 - y3)**2)))  # Distancia BC (coordenadas)
dAC = math.sqrt((((x3 - x1)**2) + ((y3 - y1)**2)))  # Distancia AC (coordenadas)

perimetro = dAB+dBC+dAC 
print('O perímetro é de {:.2f}'.format(perimetro))
