#Iniciadas por consoantes

palavras = int(input())
consoantes = 0

for e in range(palavras): 
    palavra = input().split()
    
    if palavra[0][0] not in 'aeiou':        
        consoantes += 1     

print("total de palavras: {}\niniciadas por consoantes: {} ({:.2f}%)".format(palavras, consoantes, (consoantes/palavras)*100))
