# Tabela de Quadrados

x = int(input())
y = int(input())

if x > y: 
    print("---") 
else: 
    pass 

for numero in range(x, y+1): 
    quadrado = numero**2 
    if quadrado % 3 == 0: 
        print("{} {} *".format(numero, quadrado))
    if quadrado % 3 != 0: 
        print("{} {}".format(numero, quadrado))
   
