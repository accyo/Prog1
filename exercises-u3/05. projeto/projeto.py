# UFCG - PROG1 
# KAREN A. A. ALVES - 119210934
# Seleção Projeto

cre = float(input())
ex_meses = int(input())
nota_entrevista = int(input())

if (cre < 7 and ex_meses < 6): 
    print('Candidato eliminado. CRE e experiência abaixo do limite.')
elif (cre < 7):
    print('Candidato eliminado. CRE abaixo do limite.')
elif (ex_meses < 6):
    print('Candidato eliminado. Experiência abaixo do limite.')
elif (cre >= 7 and ex_meses >= 6):
        if (nota_entrevista <= 3):
            print('Candidato classificado.')
        else:
            print('Candidato aprovado.')
