# Vogais Primeiro 

def vogais_primeiro(frase): 

    msg = '' 

    for letra in frase: 

        if letra in 'AEIOUaeiou': 
            msg += letra
        
    for letra in frase:
        
        if letra not in 'AEIOUaeiou':
            msg += letra

    return msg 

           
