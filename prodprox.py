def prodprox(vetor):

   # primeiro = vetor[0]
    
    if vetor == []: 
        return vetor

    else:
        primeiro = vetor[0] 

        for num in range(len(vetor)-1):
    
            vetor[num] *= vetor[num+1] 

        if vetor[-1]: 
        
            vetor[-1] *= primeiro  

        return vetor



