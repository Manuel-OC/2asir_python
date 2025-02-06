#Visualizar entre los valores 2 y 10 visualizar aquellos números perfectos

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
    cont = 1
    i = 2
    while (i <= N):
        print (f"Comprobando el {i}")
        if(esPerfecto(i)):
            print(f'Número perfecto {cont}: {i}')
            cont+=1
        i+=1

BuscarPerfectos(10)
