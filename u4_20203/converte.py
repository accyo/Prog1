# CONVERTE MATRICULA


matricula = input()

matricula_nova = ''

for i in range(1, len(matricula)): 
    
    if len(matricula) != 8: 
       
        break
   
    else: 

        if len(matricula_nova) == 0: 
            matricula_nova += '1' 

        matricula_nova += matricula[i]

        if len(matricula_nova) == 5: 
            matricula_nova += '0'

print(matricula_nova)
