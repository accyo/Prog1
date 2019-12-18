
comprimento = float(input())
largura = float(input())
moldura = ((comprimento/100)*2)+((largura/100)*2)
valor = moldura * 120.00

print('R$ {:.1f}'.format(valor))
