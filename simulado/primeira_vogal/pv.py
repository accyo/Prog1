# PRIMEIRA VOGAL 


palavra = input()

vogais = [] 

for vogal in range(len(palavra)):

    if palavra[vogal] in 'aeiouAEIOU': 
        vogais.append(palavra[vogal])

if vogais == []: 
    print('-')

else: 
    print(vogais[0])
