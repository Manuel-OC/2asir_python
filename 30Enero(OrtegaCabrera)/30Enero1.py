def Sumar(m1,m2):
    m3 = [[0,0,0],[0,0,0]]
    
    for i in range(0,len(m1)):
        for j in range(0,len(m1[i])):
            m3[i][j] = m1[i][j] + m2[i][j]
    
    return m3

def Visualizar1(m3):
    print(m3)

def Visualizar2(m3):
    for i in range(0,len(m3)):
        print (m3[i])
    
def Visualizar3(m3):
    for i in range(0,len(m3)):
        for j in range(0,len(m3[i])):
            print(m3[i][j])

matriz1 = [[1,2,3],[4,5,6]]
matriz2 = [[6,5,4],[3,2,1]]
matriz3 = Sumar(matriz1,matriz2)
Visualizar1(matriz3)
print("\n")
Visualizar2(matriz3)
print("\n")
Visualizar3(matriz3)
