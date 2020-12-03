# Troca Vizinhos 

def troca_vizinhos_condicional(lista): 

    troca_vizinhos = []

    for palavra in range(1, len(lista), 2): 
        
        if lista[palavra-1] > lista[palavra]:
            troca_vizinhos.append(lista[palavra])
            troca_vizinhos.append(lista[palavra-1])

        elif lista[palavra] > lista[palavra-1]:
            troca_vizinhos.append(lista[palavra-1])
            troca_vizinhos.append(lista[palavra])
    
    ultimo = lista[-1]
    
    if len(lista) % 2 != 0: 
        troca_vizinhos.append(ultimo)
    
    return troca_vizinhos


palavras = ["casa", "abacate", "boi", "casa", "jornal", "elo", "faca"]
assert troca_vizinhos_condicional(palavras) == ["abacate",  "casa", "boi", "casa", "elo", "jornal", "faca"]

palavras = ["elo", "diretor", "casa", "boi"]
assert troca_vizinhos_condicional(palavras) == ["diretor", "elo", "boi", "casa"]
