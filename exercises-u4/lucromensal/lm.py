# UFCG - PROG1
# KAREN A. A. ALVES - 119210934
# Lucro mensal 

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']

for meses in range(12): 
    mes = input().split()
    
    for lucro in range(12):
        lucro = float(mes[0]) - float(mes[1])

print(lucro)
