# UFCG - PROG1
# KAREN A. A. ALVES - 119210934
# Lei Estadual

idade = int(input('Idade? '))

if (idade < 12):
    print('criança (meia entrada')
elif (idade >= 65):
    print('idoso (meia entrada')
elif (idade >= 12 and idade < 65):
    estudante = input('Estudante? ')
        if (estudante == 's'):
            rp = input('Rede Pública? ')
                if (rp == 's'):
                    print('estudante da rede pública (isento)')
            elif (rp == 'n'):
                    print('estudante (meia entrada)')
        elif (estudante == 'n'):
            print('adulto (inteira)')
