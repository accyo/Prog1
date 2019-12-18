# UFCG - PROG1 
# KAREN A. A. ALVES - 119210934
# Validação de Triângulos

a = int(input())    # lado a do triângulo   
b = int(input())    # lado b do triângulo
c = int(input())    # lado c do triângulo
perimetro = a+b+c
condicao1 = (abs(b-c)) < a and a < (b+c)
condicao2 = (abs(a-c)) < b and b < (a+c)
condicao3 = (abs(a-b)) < c and c < (a+b)

if (condicao1 and condicao2 and condicao3):
    print('triangulo valido. {}'.format(perimetro))
else: 
    print('triangulo invalido.')
