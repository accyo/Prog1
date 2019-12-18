# UFCG 
# Prog1 
# Karen Anne Aciole Alves

lado1 = float(input())  # Entrada dos
lado2 = float(input())  # lados de um terreno 
area = float(input())   # Área de cada casa em metros quadrados 
area_terreno = lado1*lado2 
qnt_casas = area_terreno // area

print("{:0.0f} casa(s) pode(m) ser construída(s) no terreno.".format(qnt_casas))
