# UFCG 
# PROG1 
# KAREN A. A. ALVES

import math 

raio = float(input())
lado = raio * math.sqrt(2)
area_circ = math.pi * (raio**2)
area_quad = lado **2 

print('Área não comum: {:.5f}'.format(area_circ - area_quad))
