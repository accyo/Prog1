# UFCG - PROG1 
# KAREN A. A. ALVES - 119210934
# Compatibilidade Sanguínea

grupo_paciente = input() # grupo sanguineo do paciente
rh_paciente = input()      # grupo RH do paciente
grupo_doador = input()   # grupo sanguineo do doador
rh_doador = input()      # grupo RH do doador

if (grupo_paciente == 'A' and (grupo_doador == 'A' or grupo_doador == 'O')):
    if (rh_paciente == '+' and (rh_doador == '+' or rh_doador == '-')):
        print('compatível')
    elif (rh_paciente == '-' and rh_doador == '-'):
        print('compatível')
    else:
        print('incompatível')
elif (grupo_paciente == 'B' and (grupo_doador == 'B' or grupo_doador == 'O')):
    if (rh_paciente == '+' and (rh_doador == '+' or rh_doador == '-')):
        print('compatível')
    elif (rh_paciente == '-' and rh_doador == '-'):
        print('compatível')
    else: 
        print('incompatível')
elif (grupo_paciente == 'AB' and (grupo_doador == 'A' or grupo_doador == 'B' or grupo_doador == 'AB' or grupo_doador == 'O')):
    if (rh_paciente == '+' and (rh_doador == '+' or rh_doador == '-')):
        print('compatível')
    elif (rh_paciente == '-' and rh_doador == '-'):
        print('compatível')
    else: 
        print('incompatível')
elif (grupo_paciente == 'O' and grupo_doador == 'O'):
    if (rh_paciente == '+' and (rh_doador == '+' or rh_doador == '-')):
        print('compatível')
    elif(rh_paciente == '-' and rh_doador == '-'):
        print('compatível')
    else: 
        print('incompatível')
else: 
    print('incompatível')
