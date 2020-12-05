# semi cesar 

def cesar(msg, deslocamento):
    import string

    alfabeto = string.ascii_lowercase
    criptografia = ''

    for letra in msg: 
    
        for i in range(26):     # tamanho alfabeto (fixo)
        
            # pegar a posição da letra no alfabeto para fazer o deslocamento 
        
            if letra == alfabeto[i]: 
                valor_deslocamento = deslocamento + i # soma posicao da letra + número do deslocamento
            
                if valor_deslocamento > 26: # se o deslocamento ultrapassar o tamanho do alfabeto
                    valor_deslocamento = valor_deslocamento - 26 #voltar para o ínicio do alfabeto 
                
                criptografia += alfabeto[valor_deslocamento]
        
        if letra not in alfabeto:
            criptografia += letra
        
        
    return criptografia
    
assert cesar("exemplo", 4) == "ibiqtps"
assert cesar("Exemplo 2!", 4) == "Ebiqtps 2!"
assert cesar("K!!!!!!!", 6) == "K!!!!!!!"
assert cesar("k!!!!!!r", 6) == "q!!!!!!x"
assert cesar("david#bow*ie", 9) == "mjerm#kxf*rn"
