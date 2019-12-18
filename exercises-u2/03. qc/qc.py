# UFCG
# PROG1
# Karen A. A. Alves

import math 

lado = float(input())   #  lado = diametro 
r = lado / math.sqrt(2) # raiz = lado / raizquadrada(2)
area_circ = math.pi * (r**2)  # A = pi*r**2 
area_quad = lado**2 # A = lado**2
perimetro_circ = 2 * math.pi * r

print('Perímetro: {:.5f}'.format(perimetro_circ))
print('Área: {:.5f}'.format(area_circ))
