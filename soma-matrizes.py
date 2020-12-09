# Soma Matrizes

def soma_matrizes(m1, m2):
    m3 = [] 

    for i in range(len(m1)):
        m3.append([])
        for j in range(len(m1[0])):
            m3[i].append(m1[i][j] + m2[i][j])

    return m3

m1 = [
      [2, 8],
      [3, 4]
     ]

m2 = [
      [3, 2],
      [-4, 9]
     ]


assert soma_matrizes(m1, m2) == [
                                  [5, 10],
                                  [-1, 13]
                                ]
assert m1 == [
              [2, 8],
              [3, 4]
             ]

assert m2 == [
              [3, 2],
              [-4, 9]
             ]

