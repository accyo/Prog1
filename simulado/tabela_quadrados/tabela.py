 # TABELA DE QUADRADOS


x = int(input())
y = int(input())

if x > y: 
     print('---')

else: 

    for num in range(x, y+1):
        print('{} {}'.format(num, num**2))

