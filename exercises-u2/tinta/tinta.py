# UFCG - PROG1 
# KAREN A. A. ALVES - 119210934
# Tinta

altura = float(input()) 
largura = float(input())

parede = altura * largura
tinta = (parede * 3.6) / 50 

print('{:.2f} l'.format(tinta))
