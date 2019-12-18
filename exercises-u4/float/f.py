# UFCG - PROG1
# KAREN A. A. ALVES - 119210934
# Série: Sequencia de floats

inicio = 15.2
seq = 0 

for e in range(15):
    if seq == 0: 
        print(inicio)
        seq += 1
    elif seq > 0: 
        inicio -= 1.5
        seq += 1
        print('{:.1f}'.format(inicio))
