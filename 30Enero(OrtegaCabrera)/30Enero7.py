def esPerfecto(n):
    sum=0
    for i in range(n-1,0,-1):
        if n%i == 0:
            sum+=i

    if n == sum:
        return True
    else:
        return False

def BuscarPerfectos(N):
    i=1
    cont=0
    miarray=[]

    while (cont < N):
        if(esPerfecto(i)):
            miarray.append(i)
            cont+=1
        i+=1
    
    return miarray

def Visualizar(r):
    print(r)

Visualizar(BuscarPerfectos(4))