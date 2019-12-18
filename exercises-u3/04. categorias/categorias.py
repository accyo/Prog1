# UFCG - PROG1 
# KAREN A. A. ALVES - 119210934
# Categorias 

nome = input()
idade = int(input())

if (idade >= 5 and idade <= 7):
    print('{}, {} anos, Infantil A.'.format(nome, idade))
elif (idade >= 8 and idade <= 10):
    print('{}, {} anos, Infantil B.'.format(nome, idade))
elif (idade >= 11 and idade <= 13):
    print('{}, {} anos, Juvenil A.'.format(nome, idade))
elif (idade >= 14 and idade <= 17):
    print('{}, {} anos, Juvenil B.'.format(nome, idade))
elif (idade > 17): 
    print('{}, {} anos, Senior.'.format(nome,idade))
else: 
    print('{}, {} anos, Não pode competir.'.format(nome, idade))
