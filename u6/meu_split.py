# SPLIT 

def split(frase, delimitador): 

    tokens = []
    palavra = ''

    for c in frase: 
        if c not in delimitador:
            palavra += c

        elif palavra:
            tokens.append(palavra)
            palavra = ''

    if palavra:
        tokens.append(palavra)


    return tokens


assert split('um exemplo', ' ') == ['um','exemplo']
assert split('testando', 'a') == ['test', 'ndo']


