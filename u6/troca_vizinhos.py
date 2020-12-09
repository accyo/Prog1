# Troca Vizinhos 

def troca_vizinhos_condicional(seq): 

    for palavra in range(len(seq)-1): 
        
        if seq[palavra] > seq[palavra+1]:
            
            if palavra % 2 == 0:
                seq[palavra], seq[palavra+1] = seq[palavra+1], seq[palavra]

    return seq              

palavras = ["casa", "abacate", "boi", "casa", "jornal", "elo", "faca"]
troca_vizinhos_condicional(palavras)
assert palavras == ["abacate",  "casa", "boi", "casa", "elo", "jornal", "faca"]
